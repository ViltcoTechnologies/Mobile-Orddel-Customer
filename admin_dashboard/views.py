from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .models import *
from order.models import *
from payment.models import *
from client_app.models import *
from .serializers import *
from django_email_verification import sendConfirm
from datetime import datetime

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

        # Get total orders
        orders_count = OrderDetail.objects.all().count

        # Get total invoices
        invoices_count = Invoice.objects.all().count()

        # Get total clients
        client_count = Client.objects.all().count()
        # total_client_income = Client.objects.all().aggregate(average_price=Avg('total_amount_shopped'))

        # Get total delivery_persons
        delivery_person_count = DeliveryPerson.objects.all().count()


# ----------------------------------------------------------------------------------------------------------------------


# Home screen - Dashboard resources
class OrderGraphApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated, ]
    # authentication_classes = (authentication.JWTAuthentication,)

    def get(self, request):
        try:
            graph_type = self.request.query_params.get('graph_type').lower()
            print(graph_type)
            try:
                if graph_type == 'today':
                    orders_count = OrderDetail.objects.all().count
                    datetime_now = datetime.now().year
                    print(datetime_now)
                    timestamp = datetime.timestamp(datetime_now)
                    print(timestamp)
                    seconds = 24 * 60 * 60
                    timestamp_24h_ago = timestamp - seconds
                    price_dates = []
                    for candlestick in candles:
                        time = datetime.fromtimestamp(int(str(candlestick[0])[:-3]))
                        tz_conv = timezone('Etc/GMT+1').localize(time)
                        formatted_time = tz_conv.strftime("%d-%b %H:%M")
                        price_dates.append({"Closing Price": float(candlestick[4]),
                                            "Time": str(formatted_time)})
                    response = price_dates
                    print(len(candles))
                    return Response(response, status=status.HTTP_200_OK)

                if graph_type == 'daily':
                    orders_count = OrderDetail.objects.all().count
                    datetime_now = datetime.now()
                    timestamp = datetime.timestamp(datetime_now)
                    seconds = 7 * 3600 * 24
                    print(seconds)
                    print(timestamp)
                    date_7_days_back = datetime.fromtimestamp(int(timestamp - seconds)).date()
                    print(date_7_days_back)
                    candles = client.get_historical_klines("BTCEUR", Client.KLINE_INTERVAL_1DAY, str(date_7_days_back))

                    price_dates = []
                    for candlestick in candles:
                        price_dates.append({"Closing Price": float(candlestick[4]),
                                            "Date": datetime.fromtimestamp(int(str(candlestick[0])[:-3])).date().strftime(
                                                "%d %b")})

                    response = price_dates
                    print(len(candles))
                    return Response(response, status=status.HTTP_200_OK)

                if graph_type == 'weekly':
                    orders_count = OrderDetail.objects.all().count
                    datetime_now = datetime.now()
                    timestamp = datetime.timestamp(datetime_now)
                    seconds = 56 * 3600 * 24
                    print(seconds)
                    print(timestamp)
                    date_8_weeks_back = datetime.fromtimestamp(int(timestamp - seconds)).date()
                    print(date_8_weeks_back)
                    candles = client.get_historical_klines("BTCEUR", Client.KLINE_INTERVAL_1WEEK, str(date_8_weeks_back))
                    price_dates = []
                    for candlestick in candles:
                        price_dates.append({"Closing Price": float(candlestick[4]),
                                            "Date": datetime.fromtimestamp(int(str(candlestick[0])[:-3])).date().strftime(
                                                "%d %b")})

                    response = price_dates
                    print(len(candles))
                    return Response(response, status=status.HTTP_200_OK)

                if graph_type == 'monthly':
                    orders_count = OrderDetail.objects.all().count
                    datetime_now = datetime.now()
                    timestamp = datetime.timestamp(datetime_now)
                    seconds = 365 * 3600 * 24
                    print(seconds)
                    print(timestamp)
                    date_12_months_back = datetime.fromtimestamp(int(timestamp - seconds)).date()
                    print(date_12_months_back)
                    candles = client.get_historical_klines("BTCEUR", Client.KLINE_INTERVAL_1MONTH, str(date_12_months_back))
                    price_dates = []
                    for candlestick in candles:
                        price_dates.append({"Closing Price": float(candlestick[4]),
                                            "Date": datetime.fromtimestamp(int(str(candlestick[0])[:-3])).date().strftime(
                                                "%b %y")})
                    response = price_dates
                    print(len(candles))
                    return Response(response, status=status.HTTP_200_OK)

                if graph_type == 'all':
                    orders_count = OrderDetail.objects.all().count
                    datetime_now = datetime.now()
                    timestamp = datetime.timestamp(datetime_now)
                    seconds = 365 * 3600 * 24
                    print(seconds)
                    print(timestamp)
                    date_12_months_back = datetime.fromtimestamp(int(timestamp - seconds)).date()
                    print(date_12_months_back)
                    candles = client.get_historical_klines("BTCEUR", Client.KLINE_INTERVAL_1MONTH, str(date_12_months_back))
                    price_dates = []
                    for candlestick in candles:
                        price_dates.append({"Closing Price": float(candlestick[4]),
                                            "Date": datetime.fromtimestamp(int(str(candlestick[0])[:-3])).date().strftime(
                                                "%b %y")})
                    response = price_dates
                    print(len(candles))
                    return Response(response, status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_404_NOT_FOUND,
                                    data=f"'{graph_type}' is not valid graph_type, select "
                                         f"between today, daily, weekly, monthly and all")
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data="Oops! Required field graph_type is missing")


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
            try:
                _ = request.data['password']
                try:
                    serializer_class = MyTokenObtainPairSerializer(data=request.data)
                    if serializer_class.is_valid(self):
                        print("here")
                        user = User.objects.get(username=username)
                        admin_user = AdminUser.objects.get(username=username)
                        is_active = user.is_active
                        # otp_status = admin_user.otp_status
                        # approval_status = admin_user.admin_approval_status
                        print(is_active)
                        # print(otp_status)
                        # print(approval_status)
                        if is_active:
                            return Response(status=status.HTTP_200_OK, data={"admin_user_id": admin_user.id, "data": serializer_class.validated_data})
                        else:
                            return Response(status=status.HTTP_200_OK, data={"data": "delivery person not authorized"})

                    else:
                        print("invalid username and password")

                except Exception as e:
                    print(e)
                    user = User.objects.get(username=username)
                    is_active = user.is_active
                    if not is_active:
                        return Response(status=status.HTTP_400_BAD_REQUEST,
                                        data="The account is not verified via email")
                    else:
                        return Response(status=status.HTTP_400_BAD_REQUEST,
                                        data="username or password not correct")
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data="Password is required!")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data="Username is required!")


# ------------------------------------------------------------------------------------------------------------------------
