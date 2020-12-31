from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *


# Delivery Person CRUD API
class DeliveryPersonApiView(APIView):

    def get(self, request, id=None):
        return Response(status=status.HTTP_200_OK)

    def post(self, request, id=None):
        try:
            print('before')
            delivery_person = DeliveryPerson.objects.create()
            print('delivery_person')
            delivery_person.user = request.data['user']
            delivery_person.first_name = request.data['first_name']
            delivery_person.last_name = request.data['last_name']
            delivery_person.username = request.data['username']
            delivery_person.email = request.data['email']
            delivery_person.phone_number = request.data['phone_number']
            delivery_person.address = request.data['address']
            delivery_person.current_location = request.data['current_location']
            delivery_person.no_of_orders = request.data['no_of_orders']
            delivery_person.buying_capacity = request.data['buying_capacity']
            delivery_person.total_amount_shopped = request.data['total_amount_shopped']
            delivery_person.gender = request.data['gender']
            delivery_person.image = request.data['image']
            delivery_person.date_created = request.data['date_created']
            delivery_person.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data="got exception")

        return Response(status=status.HTTP_200_OK)


class VehicleRegistrationApiView(APIView):
    pass

