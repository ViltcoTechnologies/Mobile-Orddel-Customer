from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.db.models.functions import Cast
from django.db.models.fields import DateField
from .models import *
from order.models import *
from payment.models import *
from django.db.models import Count, Q, Sum
from client_app.models import *
from .serializers import *
from django_email_verification import sendConfirm
import datetime
from django.utils import timezone
import pytz
from datetime import timedelta
from dateutil.relativedelta import relativedelta
# Token Obtain pair
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# Admin Registration API
class RegisterAdminUserApiView(APIView):

    def get(self, request, id=None):
        return Response(status=status.HTTP_200_OK)

    def post(self, request, id=None):
        try:
            # optional parameters
            address = request.data['address']
            gender = request.data['gender']
            image = request.data['image']
            try:
                # required parameters
                first_name = request.data['first_name']
                last_name = request.data['last_name']
                email = request.data['email']
                username = request.data['email']
                admin_approval_status = request.data['admin_approval_status'].lower()
                phone_number = request.data['phone_number']
                password = request.data['password']
                if first_name == ""\
                        or last_name == ""\
                        or email == ""\
                        or phone_number == ""\
                        or password == "":
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data="Ooops! following required fields can't "
                                         "be empty: (first_name, last_name, email, "
                                         "phone_number, password)")
                try:
                    saved_data = User.objects.get(email=email)
                    return Response(status=status.HTTP_200_OK,
                                    data="Email already registered!")
                except:
                    try:
                        new_user = User.objects.create_user(
                            email,
                            email,
                            password
                        )
                        new_user.first_name = first_name
                        new_user.last_name = last_name
                        try:
                            new_user_details = AdminUser.objects.create(
                                user=new_user,
                                first_name=first_name,
                                last_name=last_name,
                                username=username,
                                email=email,
                                admin_approval_status=admin_approval_status,
                                phone_number=phone_number,
                                address=address,
                                gender=gender,
                                image=image
                            )
                            new_user_details.save()
                            serializer = AdminUserSerializer(new_user_details)
                            new_user.save()
                            sendConfirm(new_user)
                            return Response(status=status.HTTP_200_OK,
                                            data={"admin_user_created": serializer.data})
                        except:
                            return Response(status=status.HTTP_400_BAD_REQUEST,
                                            data="Error! admin_user was not created "
                                                 "but auth_user was created "
                                                 "deleting auth-user entry")
                    except:
                        return Response(status=status.HTTP_400_BAD_REQUEST,
                                        data="Error entering Auth-User Data")
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data="Error! Make sure you're not missing one of the "
                                     "following required fields: (first_name, last_name, "
                                     "email, admin_approval_status, phone_number, password)")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data="Error! Make sure you're not missing one of the "
                                 "following optional fields: (address, gender, image) "
                                 "Note: If you want to leave fields blank, then "
                                 "send null or empty")


# Admin User List API
class ListAdminUserApiView(APIView):

    def get(self, request, id=None):
        if id:
            try:
                admin_user = AdminUser.objects.get(id=id)
                serializer = AdminUserSerializer(admin_user)
                return Response(status=status.HTTP_200_OK,
                                data={"admin_users": serializer.data})
            except:
                return Response(status=status.HTTP_200_OK,
                                data=f"No record found against ID '{id}'!")
        else:
            try:
                admin_user = AdminUser.objects.all()
                serializer = AdminUserSerializer(admin_user, many=True)
                if not admin_user:
                    return Response(status=status.HTTP_200_OK,
                                    data={"Admin User table is empty": serializer.data})
                return Response(status=status.HTTP_200_OK,
                                data={"admin_user": serializer.data})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)


# Admin User Update API
class UpdateAdminUserApiView(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def put(self, request, id=None):
        try:
            # optional parameters
            address = request.data['address']
            gender = request.data['gender']
            image = request.data['image']
            admin_approval_status = request.data['admin_approval_status']
            phone_number = request.data['phone_number']
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            try:
                # required parameters
                email = request.data['email']
                if email == "":
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data="Ooops! email can't be empty")
                try:
                    saved_admin_user = AdminUser.objects.filter(email=email)
                    if not saved_admin_user:
                        return Response(status=status.HTTP_404_NOT_FOUND,
                                        data=f"User with email: '{email}' not found")
                    try:
                        updated_admin_user = saved_admin_user.update(
                            first_name=first_name,
                            last_name=last_name,
                            admin_approval_status=admin_approval_status,
                            phone_number=phone_number,
                            address=address,
                            gender=gender,
                            image=image
                        )
                        try:
                            saved_admin_user.user.first_name = first_name
                            saved_admin_user.user.last_name = last_name
                            serializer = AdminUserSerializer(updated_admin_user, many=True)
                            return Response(status=status.HTTP_200_OK,
                                            data={"updated_admin_user": serializer.data})
                        except:
                            return Response(status=status.HTTP_400_BAD_REQUEST,
                                            data="Error updating auth-user data")
                    except:
                        return Response(status=status.HTTP_400_BAD_REQUEST,
                                        data="Error updating admin_user Data")
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND,
                                    data="Error finding auth user data")
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data="Oops! Make sure you're not missing a required"
                                     "field (email) ")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data="Oops! Make sure following fields are not missing "
                                 "(first_name, last_name, admin approval status, "
                                 "phone_number address, gender, image) Note: If "
                                 "you want to leave fields "
                                 "blank, then send null or empty")


# Delivery Person Delete API
class DeleteAdminUserApiView(APIView):

    def get(self, request, id=None):
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        if id:
            # try:
            saved_data = AdminUser.objects.get(id=id)
            User.objects.get(id=saved_data.user.id).delete()
            return Response(status=status.HTTP_200_OK,
                            data={'Record deleted against email': saved_data.username})
            # except:
            #     return Response(status=status.HTTP_404_NOT_FOUND, data="No Record Found!")
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"Error Msg": "ID missing from URL"})


# ----------------------------------------------------------------------------------------------------------------------


# Home screen - Dashboard resources
class AdminDashboardApiView(APIView):

    def get(self, request):
        try:
            order_details = OrderDetail.objects.all()
            pending_orders = OrderDetail.objects.filter(status='pending').count()
            rejected_orders = OrderDetail.objects.filter(status='rejected').count()
            inprogress_orders = OrderDetail.objects.filter(status='in_progress').count()
            purchased_orders = OrderDetail.objects.filter(status='purchased').count()
            delivered_orders = OrderDetail.objects.filter(status='delivered').count()

            invoices = Invoice.objects.all()
            clients = Client.objects.all()
            delivery_persons = DeliveryPerson.objects.all()
            try:
                if order_details:
                    order_details = order_details.count()
                else:
                    order_details = 0
                if invoices:
                    invoices = invoices.count()
                else:
                    invoices = 0
                if clients:
                    clients = clients.count()
                    # total_client_income = clients.aggregate(average_price=Avg('total_amount_shopped'))
                else:
                    clients = 0
                if delivery_persons:
                    delivery_persons = delivery_persons.count()
                else:
                    delivery_persons = 0
                data = {
                    "total_orders": order_details,
                    "pending_orders": pending_orders,
                    "rejected_orders": rejected_orders,
                    "inprogress_orders": inprogress_orders,
                    "purchased_orders": purchased_orders,
                    "delivered_orders": delivered_orders,
                    "invoices": invoices,
                    "clients": clients,
                    "delivery_persons": delivery_persons
                }
                return Response(status=status.HTTP_200_OK,
                                data={"admin_dashboard": data})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "There was a error in calculation"})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"message": "There was a error fetching data "
                                             "from the database"})


# ----------------------------------------------------------------------------------------------------------------------

def order_stats(days=None, hours=None):
    pass


# Home screen - Dashboard resources
class OrderGraphApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated, ]
    # authentication_classes = (authentication.JWTAuthentication,)

    def get(self, request):

        def generate_stats(type_of_duration, timedelta):
            try:
                time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # converted_time_now = datetime.datetime(time_now, tzinfo=pytz.UTC)
                start_time = datetime.datetime.now()
                order_data = []
                if type_of_duration == 'hours':
                    start_time = (datetime.datetime.now() - datetime.timedelta(hours=timedelta)).strftime("%Y-%m-%d %H:%M:%S")
                    order_detail = OrderDetail.objects.filter(Q(order_created_datetime__gte=start_time), Q(order_created_datetime__lte=time_now))
                    order_data = order_detail.values('order_created_datetime').annotate(orders=Count('order_created_datetime'))
                    print(order_data)
                    
                elif type_of_duration == 'days':
                    start_time = (datetime.datetime.now() - datetime.timedelta(days=timedelta)).strftime("%Y-%m-%d %H:%M:%S")
                    order_detail = OrderDetail.objects.filter(Q(order_created_datetime__gte=start_time), Q(order_created_datetime__lte=time_now))
                    order_data = order_detail.values('order_created_datetime').annotate(orders=Count('order_created_datetime'))
                    order_data = order_data.annotate(date_only=Cast('order_created_datetime', DateField())).values('date_only').annotate(orders_count=Count('date_only'))

                elif type_of_duration == 'weeks':
                    start_time = (datetime.datetime.now() - datetime.timedelta(weeks=timedelta)).strftime("%Y-%m-%d %H:%M:%S")
                    order_detail = OrderDetail.objects.filter(Q(order_created_datetime__gte=start_time), Q(order_created_datetime__lte=time_now))
                    order_data = order_detail.values('order_created_datetime').annotate(orders=Count('order_created_datetime'))
                    order_data = order_data.annotate(date_only=Cast('order_created_datetime', DateField())).values('date_only').annotate(orders_count=Count('date_only'))

                elif type_of_duration == 'months':
                    start_time = (datetime.datetime.now() - relativedelta(months=timedelta)).strftime("%Y-%m-%d %H:%M:%S")
                    order_detail = OrderDetail.objects.filter(Q(order_created_datetime__gte=start_time), Q(order_created_datetime__lte=time_now))
                    order_data = order_detail.values('order_created_datetime').annotate(orders=Count('order_created_datetime'))
                    order_data = order_data.annotate(date_only=Cast('order_created_datetime', DateField())).values('date_only').annotate(orders_count=Count('date_only'))
                # converted_start_time = datetime.datetime(start_time, tzinfo=pytz.UTC)
                elif type_of_duration == 'years':
                    start_time = (datetime.datetime.now() - relativedelta(years=timedelta)).strftime("%Y-%m-%d %H:%M:%S")
                    print(start_time)
                    order_detail = OrderDetail.objects.filter(Q(order_created_datetime__gte=start_time), Q(order_created_datetime__lte=time_now))
                    order_data = order_detail.values('order_created_datetime').annotate(orders=Count('order_created_datetime'))
                    order_data = order_data.annotate(date_only=Cast('order_created_datetime', DateField())).values('date_only').annotate(orders_count=Count('date_only'))

                elif type_of_duration == 'all':
                    order_detail = OrderDetail.objects.all()
                    order_data = order_detail.values('order_created_datetime').annotate(orders=Count('order_created_datetime'))
                    order_data = order_data.annotate(date_only=Cast('order_created_datetime', DateField())).values('date_only').annotate(orders_count=Count('date_only'))

                response = []
                for order in order_data:
                    try:
                        response.append({"date": order['date_only'].strftime('%Y-%m-%d %H:%M:%S')[0:10],
                                         "orders": order['orders_count']
                                         })
                    except:
                        response.append({"order_created_datetime": order['order_created_datetime'].strftime('%Y-%m-%d %H:%M:%S'),
                                         "orders": order['orders']
                                         })
                return response

            except Exception as e:
                print(e)
                return Response(status=status.HTTP_400_BAD_REQUEST)

        graph_type = self.request.query_params.get('graph_type').lower()
        print(graph_type)

        try:
            if graph_type == '24h':
                response = generate_stats('hours', 24)
                return Response(status=status.HTTP_200_OK, data={'response': response})

            if graph_type == 'daily':
                response = generate_stats('days', 7)
                return Response(status=status.HTTP_200_OK, data={'response': response})

            if graph_type == 'weekly':
                response = generate_stats('weeks', 4)
                return Response(status=status.HTTP_200_OK, data={'response': response})

            if graph_type == 'monthly':
                response = generate_stats('months', 12)
                return Response(status=status.HTTP_200_OK, data={'response': response})

            if graph_type == 'yearly':
                response = generate_stats('years', 4)
                return Response(status=status.HTTP_200_OK, data={'response': response})
            if graph_type == 'all':
                response = generate_stats('all', 0)
                return Response(status=status.HTTP_200_OK, data={'response': response})

            return Response(status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
# ----------------------------------------------------------------------------------------------------------------------


# Client signup approval log
class CreateClientApprovalLog(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def put(self, request, id=None):
        try:
            # required parameters
            client_id = request.data['client']
            admin_id = request.data['admin']
            admin_approval_status = request.data['admin_approval_status']
            if client_id == ""\
                    and admin_id == ""\
                    and admin_approval_status == "":
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data="Ooops! id of client, admin and admin_approval_status "
                                     "can't be empty")
            try:
                new_approval_log = ClientApprovalLog.objects.create(
                    client=client_id,
                    admin=admin_id,
                    admin_approval_status=admin_approval_status
                )
                serializer = ClientApprovalLogSerializer(new_approval_log)
                return Response(status=status.HTTP_200_OK,
                                data={"log_created": serializer.data})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data="Error creating client approval log")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data="Oops! Make sure you're not missing one or more required"
                                 "fields (id of client, admin and admin_approval_status) ")


# Delivery Person signup approval log
class CreateDeliveryPersonApprovalLog(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def put(self, request, id=None):
        try:
            # required parameters
            delivery_person_id = request.data['delivery_person']
            admin_id = request.data['admin']
            admin_approval_status = request.data['admin_approval_status']
            if delivery_person_id == ""\
                    and admin_id == ""\
                    and admin_approval_status == "":
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data="Ooops! id of delivery_person, admin "
                                     "and admin_approval_status can't be empty")
            try:
                new_approval_log = DeliveryPersonApprovalLog.objects.create(
                    delivery_person=delivery_person_id,
                    admin=admin_id,
                    admin_approval_status=admin_approval_status
                )
                serializer = DeliveryPersonApprovalLogSerializer(new_approval_log)
                return Response(status=status.HTTP_200_OK,
                                data={"log_created": serializer.data})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data="Error creating client approval log")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data="Oops! Make sure you're not missing one or more required"
                                 "fields (id of client, admin and admin_approval_status) ")


# ------------------------------------------------------------------------------------------------------------------------

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        return data


# ------------------------------------------------------------------------------------------------------------------------

class AdminLogin(TokenObtainPairView):

    def post(self, request):
        # print(request.data)
        try:
            username = request.data['username']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"message": "Username is required!"})
        try:
            _ = request.data['password']
        
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Password is required!"})
        try:
            serializer_class = MyTokenObtainPairSerializer(data=request.data)
            if serializer_class.is_valid(self):
                print("here")
                try:
                    user = User.objects.get(username=username)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'User does not exist'})
                admin_user = AdminUser.objects.get(username=username)
                is_active = user.is_active
                # otp_status = admin_user.otp_status
                # approval_status = admin_user.admin_approval_status
                print(is_active)
                # print(otp_status)
                # print(approval_status)
                if is_active:
                    response = serializer_class.validated_data
                    response["admin_user_id"] = admin_user.id
                    return Response(status=status.HTTP_200_OK, data={"data": response})
                else:
                    return Response(status=status.HTTP_200_OK, data={"data": "admin user not authorized"})

            else:
                print("invalid username and password")

        except Exception as e:
            print(e)
            try:
                user = User.objects.get(username=username)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'User does not exist'})

            is_active = user.is_active
            if not is_active:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "The account is not verified via email"})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "username or password not correct"})
            
        


# ------------------------------------------------------------------------------------------------------------------------
