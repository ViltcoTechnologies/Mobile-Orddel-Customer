from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt import authentication
from django_email_verification import sendConfirm
from rest_framework.response import Response
from .models import *
from .serializers import *


class ClientRegisterApiView(APIView):

    def post(self, request, id=None):
        try:
            saved_data = User.objects.get(email=request.data['email'])
            return Response(status=status.HTTP_200_OK, data="Email already registered!")

        except:
            try:
                new_user = User.objects.create_user(
                    request.data['username'], request.data['email'], request.data['password'])
                new_user.first_name = request.data['first_name']
                new_user.last_name = request.data['last_name']
                new_user.save()
                sendConfirm(new_user)
                saved_data = User.objects.get(username=request.data['username'])

                try:
                    new_user_details = Client.objects.create(
                        user_id=saved_data.id,
                        first_name=request.data['first_name'],
                        last_name = request.data['last_name'],
                        username = request.data['username'],
                        email=request.data['email'],
                        phone_number = request.data['phone_number'],
                        address = request.data['address'],
                        current_location = request.data['current_location'],
                        gender = request.data['gender'],
                        image = request.data['image'],
                        # number_of_order = request.data['number_of_order'],
                        # total_amount_shopped = request.data['total_amount_shopped'],

                    )
                    data_to_pass = Client.objects.get(
                        username=saved_data.username)
                    serializer = ClientSerializer(data_to_pass)
                    return Response(status=status.HTTP_200_OK, data={"local_account_data": serializer.data})
                except AssertionError as err:
                    return Response(status=status.HTTP_200_OK, data=err)
            except AssertionError as err:
                return Response(status=status.HTTP_404_NOT_FOUND, data=err)


class UpdateClientApiView(APIView):

    def get(self, request):
        saved_data = Client.objects.get(email=request.data['email'])
        data_to_pass = ClientSerializer(saved_data)
        return Response(status=status.HTTP_200_OK, data={"Fetched Data": data_to_pass.data})

    def put(self, request, id=None):
        try:
            saved_data = User.objects.get(email=request.data['email'])
            saved_data.first_name = request.data['first_name']
            saved_data.last_name = request.data['last_name']
            # saved_data.password = request.data['password']
            Client.objects.filter(user_id = saved_data.id).update(
                    first_name = request.data["first_name"],
                    last_name = request.data["last_name"],
                    phone_number = request.data["phone_number"],
                    address = request.data["address"],
                    current_location = request.data["current_location"],
                    gender = request.data["gender"],
                    image = request.data["image"]
            )
            saved_data.save()
            data_to_pass = Client.objects.get(username=saved_data.username)
            serializer = ClientSerializer(data_to_pass)
            return Response(status=status.HTTP_200_OK, data={"Updated details": serializer.data})
        except AssertionError as err:
            return Response(status=status.HTTP_404_NOT_FOUND, data=err)


class DeleteClientApiView(APIView):

    def delete(self,  request):
        try:
            client = User.objects.get(email = request.data['email'])
            email = client.email
            client.delete()
            return Response(status=status.HTTP_200_OK, data={"Deleted record against email": email})
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST, data={"Exception" : e})

class ListClientsApiView(APIView):

    def get(self, request):
        try:
            clients = Client.objects.all()
            data_to_pass = ClientSerializer(clients, many=True)
            return Response(status=status.HTTP_200_OK, data={"All Clients": data_to_pass.data})
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"No Clients Found"})
