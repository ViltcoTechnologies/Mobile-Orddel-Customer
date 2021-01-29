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
                        sendConfirm(new_user)
                        try:
                            new_user_details = AdminUser.objects.create(
                                user=new_user,
                                first_name=first_name,
                                last_name=last_name,
                                username=username,
                                email=email,
                                phone_number=phone_number,
                                address=address,
                                gender=gender,
                                image=image
                            )
                            new_user_details.save()
                            serializer = AdminUserSerializer(new_user_details)
                            new_user.save()
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
                                     "email, phone_number, password)")
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
                                 "(first_name, last_name, phone_number address, "
                                 "gender, image) Note: If you want to leave fields "
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

        # Get orders
        # order_data = OrderDetail.objects.all()

        # Get invoices
        invoice_data = Invoice.objects.all().count()
        print(invoice_data)

        # Get clients
        client_data = Client.objects.all().count()
        total_client_income = Client.objects.all().aggregate(average_price=Avg('total_amount_shopped'))

        # Get delivery_persons
        delivery_person_data = DeliveryPerson.objects.all().count()
        print(delivery_person_data)


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
