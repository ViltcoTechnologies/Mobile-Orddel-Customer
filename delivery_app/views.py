from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django_email_verification import sendConfirm


# Delivery Person CRUD API
class DeliveryPersonApiView(APIView):

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
                    new_user_details = DeliveryPerson.objects.create(
                        user=new_user,
                        first_name=request.data['first_name'],
                        last_name=request.data['last_name'],
                        username=request.data['username'],
                        email=request.data['email'],
                        phone_number=request.data['phone_number'],
                        address=request.data['address'],
                        current_location=request.data['current_location'],
                        buying_capacity=request.data['buying_capacity'],
                        gender=request.data['gender'],
                        image=request.data['image'],
                        date_created=request.data['date_created'])
                    new_user.save()
                    data_to_pass = DeliveryPerson.objects.get(username=new_user.username)
                    serializer = DeliveryPersonSerializer(data_to_pass)
                    return Response(status=status.HTTP_200_OK, data={"local_account_data": serializer.data})
                except AssertionError as err:
                    return Response(status=status.HTTP_200_OK, data=err)
            except AssertionError as err:
                return Response(status=status.HTTP_404_NOT_FOUND, data=err)


class VehicleRegistrationApiView(APIView):
    pass

