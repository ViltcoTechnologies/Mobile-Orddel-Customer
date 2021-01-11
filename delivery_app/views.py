from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django_email_verification import sendConfirm


# Delivery Person Registration API
class RegisterDeliveryPersonApiView(APIView):

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
class ListDeliveryPersonApiView(APIView):

    def get(self, request, id=None):
        if id:
            try:
                delivery_person = DeliveryPerson.objects.get(id=id)
                serializer = DeliveryPersonSerializer(delivery_person)
                return Response(status=status.HTTP_200_OK, data={"admin_user": serializer.data})
            except:
                return Response(status=status.HTTP_200_OK, data="Database is empty!")
        else:
            try:
                delivery_person = DeliveryPerson.objects.all()
                serializer = DeliveryPersonSerializer(delivery_person, many=True)
                return Response(status=status.HTTP_200_OK, data={"admin_users": serializer.data})
            except:
                return Response(status=status.HTTP_200_OK, data="Database is empty!")


# Delivery Person Update API
class UpdateDeliveryPersonApiView(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def put(self, request, id=None):
        try:
            saved_auth_user = User.objects.get(email=request.data['email'])
            saved_auth_user.first_name = request.data['first_name']
            saved_auth_user.last_name = request.data['last_name']

            saved_data = DeliveryPerson.objects.filter(user_id=saved_auth_user.id)
            saved_data.update(
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                phone_number=request.data['phone_number'],
                address=request.data['address'],
                current_location=request.data['current_location'],
                buying_capacity=request.data['buying_capacity'],
                gender=request.data['gender'],
                image=request.data['image'],
                date_created=request.data['date_created']
            )
            serializer = DeliveryPersonSerializer(saved_data, many=True)
            return Response(status=status.HTTP_200_OK, data={'updated_delivery_person': serializer.data})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data="No Record Found!")


# Delivery Person Delete API
class DeleteDeliveryPersonApiView(APIView):

    def get(self, request, id=None):
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        if id:
            try:
                saved_data = DeliveryPerson.objects.get(id=id)
                User.objects.get(id=saved_data.user.id).delete()
                return Response(status=status.HTTP_200_OK, data={'Record deleted against email': saved_data.username})
            except:
                return Response(status=status.HTTP_404_NOT_FOUND, data="No Record Found!")
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Error Msg": "ID missing from URL"})


# ------------------------------------------------------------------------------------------------------------------------


# Vehicle Registration API
class RegisterVehicleApiView(APIView):

    def get(self, request, id=None):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        try:
            saved_data = Vehicle.objects.get(registration_no=request.data['registration_no'])
            return Response(status=status.HTTP_200_OK, data="Vehicle already registered!")
        except:
            try:
                delivery_person = DeliveryPerson.objects.get(id=request.data['delivery_person'])
                try:
                    new_vehicle_details = Vehicle.objects.create(
                        delivery_person=delivery_person,
                        make=request.data['make'],
                        model=request.data['model'],
                        color=request.data['color'],
                        year=request.data['year'],
                        registration_no=request.data['registration_no'],
                        license_image_front=request.data['license_image_front'],
                        license_image_back=request.data['license_image_back'],
                        copy_image_front=request.data['copy_image_front'],
                        copy_image_back=request.data['copy_image_back'],
                        license_no=request.data['license_no'],
                        date_created=request.data['date_created']
                    )
                    new_vehicle_details.save()
                    serializer = VehicleSerializer(new_vehicle_details)
                    return Response(status=status.HTTP_200_OK, data={"vehicle_registered": serializer.data})
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data="There was a error creating record!")
            except:
                return Response(status=status.HTTP_404_NOT_FOUND, data="Vehicle Already Registered!")


# Vehicle List API
class ListVehicleApiView(APIView):

    def get(self, request, id=None):
        if id:
            try:
                vehicle = Vehicle.objects.get(id=id)
                serializer = VehicleSerializer(vehicle)
                return Response(status=status.HTTP_200_OK, data={id: serializer.data})
            except:
                return Response(status=status.HTTP_404_NOT_FOUND, data={"No Vehicle with ID!": id})
        else:
            try:
                vehicle = Vehicle.objects.all()
                serializer = VehicleSerializer(vehicle, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND, data="Database is empty!")


# Vehicle ID based Vehicle List API
class ListDeliveryPersonVehicleApiView(APIView):

    def get(self, request, id=None):
        if id:
            try:
                vehicle = Vehicle.objects.filter(delivery_person__id=id)
                serializer = VehicleSerializer(vehicle, many=True)
                return Response(status=status.HTTP_200_OK,
                                data={"user_vehicles": serializer.data})
            except:
                return Response(status=status.HTTP_404_NOT_FOUND,
                                data="No User Vehicle in Database!")
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"Error Msg": "ID missing from URL"})


# Vehicle Update API
class UpdateVehicleApiView(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def put(self, request, id=None):
        try:
            saved_vehicle_data = Vehicle.objects.filter(registration_no=request.data['registration_no'])
            try:
                saved_vehicle_data.update(
                    make=request.data['make'],
                    model=request.data['model'],
                    color=request.data['color'],
                    year=request.data['year'],
                    license_image_front=request.data['license_image_front'],
                    license_image_back=request.data['license_image_back'],
                    copy_image_front=request.data['copy_image_front'],
                    copy_image_back=request.data['copy_image_back'],
                    license_no=request.data['license_no']
                )
                serializer = VehicleSerializer(saved_vehicle_data, many=True)
                return Response(status=status.HTTP_200_OK,
                                data={'changes_updated': serializer.data})
            except:
                return Response(status=status.HTTP_404_NOT_FOUND,
                                data='There was a error updating the data!')
        except:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data=f"No record found against {request.data['registration_no']}")


# Vehicle Delete API
class DeleteVehicleApiView(APIView):

    def get(self, request, id=None):
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        if id:
            try:
                saved_data = Vehicle.objects.get(id=id)
                registration_no = saved_data.registration_no
                saved_data.delete()
                return Response(status=status.HTTP_200_OK,
                                data={'Record deleted against Vehicle Registration Number': registration_no})
            except:
                return Response(status=status.HTTP_404_NOT_FOUND, data="No Record Found!")
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"Error Msg": "ID missing from URL"})

