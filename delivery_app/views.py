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
            # optional parameters
            buying_capacity = request.data['buying_capacity']
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
                        new_auth_user = User.objects.create_user(
                            email,
                            email,
                            password
                        )
                        new_auth_user.first_name = first_name
                        new_auth_user.last_name = last_name
                        sendConfirm(new_auth_user)
                        try:
                            new_delivery_person = DeliveryPerson.objects.create(
                                user=new_auth_user,
                                first_name=first_name,
                                last_name=last_name,
                                username=username,
                                email=email,
                                buying_capacity=buying_capacity,
                                phone_number=phone_number,
                                address=address,
                                gender=gender,
                                image=image
                            )
                            new_delivery_person.save()
                            serializer = DeliveryPersonSerializer(new_delivery_person)
                            new_auth_user.save()
                            return Response(status=status.HTTP_200_OK,
                                            data={"delivery_person_created": serializer.data})
                        except:
                            return Response(status=status.HTTP_400_BAD_REQUEST,
                                            data="Error! delivery_person was not created "
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
                            data="Error! Make sure you're not missing one "
                                 "of the following optional fields: "
                                 "(buying_capacity, address, gender, image) "
                                 "Note: If you want to leave fields blank, then "
                                 "send null or empty")


# Delivery Person List API
class ListDeliveryPersonApiView(APIView):

    def get(self, request, id=None):
        if id:
            try:
                delivery_person = DeliveryPerson.objects.get(id=id)
                serializer = DeliveryPersonSerializer(delivery_person)
                return Response(status=status.HTTP_200_OK,
                                data={"delivery_persons": serializer.data})
            except:
                return Response(status=status.HTTP_200_OK,
                                data=f"No record found against ID '{id}'!")
        else:
            try:
                delivery_person = DeliveryPerson.objects.all()
                serializer = DeliveryPersonSerializer(delivery_person, many=True)
                if not admin_user:
                    return Response(status=status.HTTP_200_OK,
                                    data={"Delivery Person table is empty": serializer.data})
                return Response(status=status.HTTP_200_OK,
                                data={"delivery_person": serializer.data})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)


# Delivery Person Update API
class UpdateDeliveryPersonApiView(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def put(self, request, id=None):
        try:
            # optional parameters
            buying_capacity = request.data['buying_capacity']
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
                    saved_delivery_person = DeliveryPerson.objects.filter(email=email)
                    if not saved_delivery_person:
                        return Response(status=status.HTTP_404_NOT_FOUND,
                                        data=f"delivery_person with email: '{email}' not found")
                    try:
                        updated_delivery_person = saved_delivery_person.update(
                            first_name=first_name,
                            last_name=last_name,
                            phone_number=phone_number,
                            buying_capacity=buying_capacity,
                            address=address,
                            gender=gender,
                            image=image
                        )
                        try:
                            saved_delivery_person.user.first_name = first_name
                            saved_delivery_person.user.last_name = last_name
                            serializer = DeliveryPersonSerializer(updated_delivery_person, many=True)
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
                                 "(first_name, last_name, phone_number, buying_capacity "
                                 "address, gender, image) Note: If you want to "
                                 "leave fields blank, then send null or empty")


# Delivery Person Delete API
class DeleteDeliveryPersonApiView(APIView):

    def get(self, request, id=None):
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        if id:
            try:
                saved_data = DeliveryPerson.objects.get(id=id)
                User.objects.get(id=saved_data.user.id).delete()
                return Response(status=status.HTTP_200_OK,
                                data={'Record deleted against email': saved_data.username})
            except:
                return Response(status=status.HTTP_404_NOT_FOUND,
                                data="No Record Found!")
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"Error Msg": "ID missing from URL"})


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
                        license_no=request.data['license_no']
                    )
                    new_vehicle_details.save()
                    serializer = VehicleSerializer(new_vehicle_details)
                    return Response(status=status.HTTP_200_OK, data={"vehicle_registered": serializer.data})
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data="There was a error creating record!")
            except:
                return Response(status=status.HTTP_404_NOT_FOUND, data="Invalid Delivery Person ID!")


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

