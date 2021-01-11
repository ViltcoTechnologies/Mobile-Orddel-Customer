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
            saved_data = User.objects.get(email=request.data['email'])
            return Response(status=status.HTTP_200_OK, data="Email already registered!")
        except:
            try:
                new_user = User.objects.create_user(
                    request.data['username'],
                    request.data['email'],
                    request.data['password']
                )
                new_user.first_name = request.data['first_name']
                new_user.last_name = request.data['last_name']
                sendConfirm(new_user)
                # saved_data = User.objects.get(username=request.data['username'])

                try:
                    new_user_details = AdminUser.objects.create(
                        user=new_user,
                        first_name=request.data['first_name'],
                        last_name=request.data['last_name'],
                        username=request.data['username'],
                        email=request.data['email'],
                        phone_number=request.data['phone_number'],
                        address=request.data['address'],
                        gender=request.data['gender'],
                        image=request.data['image'],
                        date_created=request.data['date_created']
                    )
                    new_user.save()
                    data_to_pass = DeliveryPerson.objects.get(username=new_user.username)
                    serializer = DeliveryPersonSerializer(data_to_pass)
                    return Response(status=status.HTTP_200_OK, data={"local_account_data": serializer.data})
                except AssertionError as err:
                    return Response(status=status.HTTP_200_OK, data=err)
            except AssertionError as err:
                return Response(status=status.HTTP_404_NOT_FOUND, data=err)


# Delivery Person List API
class ListAdminUserApiView(APIView):

    def get(self, request, id=None):
        if id:
            try:
                admin_user = AdminUser.objects.get(id=id)
                serializer = AdminUserSerializer(admin_user)
                return Response(status=status.HTTP_200_OK, data={"admin_user": serializer.data})
            except:
                return Response(status=status.HTTP_200_OK, data="Database is empty!")
        else:
            try:
                admin_user = AdminUser.objects.all()
                serializer = AdminUserSerializer(admin_user, many=True)
                return Response(status=status.HTTP_200_OK, data={"admin_user": serializer.data})
            except:
                return Response(status=status.HTTP_200_OK, data="Database is empty!")


# Delivery Person Update API
class UpdateAdminUserApiView(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def put(self, request, id=None):
        try:
            saved_auth_user = User.objects.get(email=request.data['email'])
            saved_auth_user.first_name = request.data['first_name']
            saved_auth_user.last_name = request.data['last_name']

            saved_data = AdminUser.objects.filter(user_id=saved_auth_user.id)
            saved_data.update(
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                phone_number=request.data['phone_number'],
                address=request.data['address'],
                gender=request.data['gender'],
                image=request.data['image'],
                date_created=request.data['date_created']
            )
            serializer = AdminUserSerializer(saved_data, many=True)
            return Response(status=status.HTTP_200_OK, data={'updated_admin_user': serializer.data})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data="No Record Found!")


# Delivery Person Delete API
class DeleteAdminUserApiView(APIView):

    def get(self, request, id=None):
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        if id:
            # try:
            saved_data = AdminUser.objects.get(id=id)
            User.objects.get(id=saved_data.user.id).delete()
            return Response(status=status.HTTP_200_OK, data={'Record deleted against email': saved_data.username})
            # except:
            #     return Response(status=status.HTTP_404_NOT_FOUND, data="No Record Found!")
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Error Msg": "ID missing from URL"})


# ----------------------------------------------------------------------------------------------------------------------


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

