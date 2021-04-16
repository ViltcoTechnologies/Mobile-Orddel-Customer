from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework_simplejwt import authentication
from fcm_django.models import FCMDevice
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from client_app.models import *
from order.models import *
from admin_dashboard.models import *
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from .serializers import *
from admin_dashboard.serializers import *
from django_email_verification import sendConfirm
from django.core.mail import send_mail
from ordel.verificaton import TwilioVerification
import datetime
from datetime import date
from django.shortcuts import get_object_or_404
# Token Obtain pair
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# Delivery Person home screen Dashboard
class DeliveryPersonDashboardApiView(APIView):

    def get(self, request, id=None):
        try:
            delivery_person_id = id
            if delivery_person_id == "":
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "delivery_person can't be empty"})
            try:
                delivery_person = DeliveryPerson.objects.get(id=delivery_person_id)
                try:
                    delivery_person_package_log = DeliveryPersonPackageLog.objects.filter(delivery_person=delivery_person).last()
                    if delivery_person_package_log.date_expiry <= date.today():
                        remaining_invoices = 0
                        delivery_person_package = "_"

                    else:
                        remaining_invoices = delivery_person.no_of_invoices
                        delivery_person_package = delivery_person.package.name
                    delivery_person_image = delivery_person.image
                    delivery_person_name = f"{delivery_person.first_name} {delivery_person.last_name}"
                    
                    total_invoices = delivery_person.package.no_of_invoices
                    
                    # used_invoices = total_invoices - remaining_invoices
                    # if used_invoices < 0:
                    #     used_invoices = 0
                    used_invoices = delivery_person.used_invoices
                    no_of_pending_orders = OrderDetail.objects.filter(status="pending", delivery_person=delivery_person_id)
                    no_of_completed_orders = OrderDetail.objects.filter(status="delivered", delivery_person=delivery_person_id)
                    no_of_in_progress_orders = OrderDetail.objects.filter(status="in_progress", delivery_person=delivery_person_id)
                    if no_of_pending_orders:
                        no_of_pending_orders = no_of_pending_orders.count()
                    else:
                        no_of_pending_orders = 0
                    if no_of_completed_orders:
                        no_of_completed_orders = no_of_completed_orders.count()
                    else:
                        no_of_completed_orders = 0
                    if no_of_in_progress_orders:
                        no_of_in_progress_orders = no_of_in_progress_orders.count()
                    else:
                        no_of_in_progress_orders = 0
                    data = {
                        # "delivery_person_image": delivery_person_image,
                        "delivery_person_name": delivery_person_name,
                        "delivery_person_package": delivery_person_package,
                        "delivery_person_first_name": delivery_person.first_name, 
                        "delivery_person_last_name": delivery_person.last_name, 
                        "delivery_person_phone": delivery_person.phone_number,
                        "delivery_person_user_name": delivery_person.username,
                        "delivery_person_address": delivery_person.address, 
                        "delivery_person_package": delivery_person_package.capitalize(),
                        "total_invoices": total_invoices,
                        "remaining_invoices": remaining_invoices,
                        "used_invoices": used_invoices,
                        "no_of_pending_orders": no_of_pending_orders,
                        "no_of_completed_orders": no_of_completed_orders,
                        "no_of_in_progress_orders": no_of_in_progress_orders
                    }
                    return Response(status=status.HTTP_200_OK,
                                    data={"delivery_person_dashboard": data})
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data={"message": "There was a error fetching data "
                                                     "from the database"})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "Incorrect Delivery Person ID"})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"message": "client is required"})


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
            current_location = request.data['current_location']
            try:
                # required parameters
                first_name = request.data['first_name']
                last_name = request.data['last_name']
                email = request.data['email']
                username = request.data['email']
                phone_number = request.data['phone_number']
                password = request.data['password']
                admin_approval_status = 'pending'
                package = request.data['package']
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
                    saved_data = DeliveryPerson.objects.get(phone_number=phone_number)
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data="Phone Number already registered!")
                except:

                    try:
                        package = DeliveryPersonPackage.objects.get(id=package)
                        no_of_invoices = package.no_of_invoices
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
                                    package=package,
                                    first_name=first_name,
                                    last_name=last_name,
                                    username=username,
                                    admin_approval_status=admin_approval_status,
                                    email=email,
                                    current_location=current_location,
                                    buying_capacity=buying_capacity,
                                    phone_number=phone_number,
                                    address=address,
                                    gender=gender,
                                    image=image,
                                    no_of_invoices=no_of_invoices,
                                )
                                try:
                                    twilio_verification = TwilioVerification(str(phone_number))
                                    twilio_verification.send_otp()
                                    try:
                                        sendConfirm(new_auth_user)
                                    except:
                                        return Response(status=status.HTTP_400_BAD_REQUEST,
                                                        data={"message": "There was an error sending verification "
                                                                         "email"})
                                except:
                                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                                    data={"message": "There was an error sending otp "
                                                                     "please try to sign up again"})
                                new_delivery_person.save()
                                serializer = DeliveryPersonSerializer(new_delivery_person)
                                new_auth_user.save()

                                return Response(status=status.HTTP_200_OK,
                                                data={"delivery_person_created": serializer.data})
                            except:
                                return Response(status=status.HTTP_400_BAD_REQUEST,
                                                data={"message": "there was an error "
                                                                 "creating delivery person"})
                        except:
                            return Response(status=status.HTTP_400_BAD_REQUEST,
                                            data={"message": "User already exists"})
                    except:
                        return Response(status=status.HTTP_404_NOT_FOUND,
                                        data={"message": f"No package with the ID: {package}"})

            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "Make sure you're not missing one of the "
                                      "following required fields: (first_name, last_name, "
                                      "email, phone_number, password)"})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data="Error! Make sure you're not missing one "
                                 "of the following optional fields: "
                                 "(buying_capacity, address, gender,"
                                 "current_location, image) "
                                 "Note: If you want to leave fields blank, then "
                                 "send null or empty")


class RegisterDeliveryPersonApiViewV2(APIView):

    def get(self, request, id=None):
        return Response(status=status.HTTP_200_OK)

    def post(self, request, id=None):
        try:
            # optional parameters
            buying_capacity = request.data['buying_capacity']
            address = request.data['address']
            gender = request.data['gender']
            image = request.data['image']
            current_location = request.data['current_location']
            try:
                # required parameters
                first_name = request.data['first_name']
                last_name = request.data['last_name']
                email = request.data['email']
                username = request.data['email']
                phone_number = request.data['phone_number']
                password = request.data['password']
                otp_status = request.data['otp_status']
                admin_approval_status = 'pending'
                package = request.data['package']
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
                    saved_data = DeliveryPerson.objects.get(phone_number=phone_number)
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data="Phone Number already registered!")
                except:

                    try:
                        package = DeliveryPersonPackage.objects.get(id=package)
                        no_of_invoices = package.no_of_invoices
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
                                    package=package,
                                    first_name=first_name,
                                    last_name=last_name,
                                    otp_status=otp_status,
                                    username=username,
                                    admin_approval_status=admin_approval_status,
                                    email=email,
                                    current_location=current_location,
                                    buying_capacity=buying_capacity,
                                    phone_number=phone_number,
                                    address=address,
                                    gender=gender,
                                    image=image,
                                    no_of_invoices=no_of_invoices,
                                )
                                try:
                                    DeliveryPersonPackageLog.objects.create(
                                        delivery_person=new_delivery_person,
                                        package=package,
                                        date_expiry=datetime.datetime.now() + datetime.timedelta(
                                            package.validity_in_days),
                                        status='active'
                                    )
                                except:
                                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                                    data={'message': 'Unable to create Delivery '
                                                                     'Person Package Log'})
                                try:
                                    sendConfirm(new_auth_user)
                                except:
                                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                                    data={"message": "There was an error sending verification "
                                                                     "email"})

                                new_delivery_person.save()
                                serializer = DeliveryPersonSerializer(new_delivery_person)
                                new_auth_user.save()

                                return Response(status=status.HTTP_200_OK,
                                                data={"delivery_person_created": serializer.data})
                            except:
                                return Response(status=status.HTTP_400_BAD_REQUEST,
                                                data={"message": "there was an error "
                                                                 "creating delivery person"})
                        except:
                            return Response(status=status.HTTP_400_BAD_REQUEST,
                                            data={"message": "User already exists"})
                    except:
                        return Response(status=status.HTTP_404_NOT_FOUND,
                                        data={"message": f"No package with the ID: {package}"})

            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "Make sure you're not missing one of the "
                                      "following required fields: (first_name, last_name, "
                                      "email, phone_number, password)"})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data="Error! Make sure you're not missing one "
                                 "of the following optional fields: "
                                 "(buying_capacity, address, gender,"
                                 "current_location, image) "
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
                                data={"delivery_person": serializer.data})
            except:
                return Response(status=status.HTTP_200_OK,
                                data=f"No record found against ID '{id}'!")
        else:
            try:
                delivery_person = DeliveryPerson.objects.all()
                serializer = DeliveryPersonSerializer(delivery_person, many=True)
                if not delivery_person:
                    return Response(status=status.HTTP_200_OK,
                                    data={"Delivery Person table is empty": serializer.data})
                return Response(status=status.HTTP_200_OK,
                                data={"delivery_person": serializer.data})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)


# Delivery Person Update API
# class UpdateDeliveryPersonApiView(APIView):
#     # permission_classes = [permissions.IsAuthenticated, ]
#     # authentication_classes = (authentication.JWTAuthentication,)

#     def get(self, request):
#         return Response(status=status.HTTP_200_OK)

#     def put(self, request, id=None):
#         try:
#             # optional parameters
#             first_name = request.data['first_name']
#             last_name = request.data['last_name']
#             phone_number = request.data['phone_number']
#             address = request.data['address']
#             # current_location = request.data['current_location']
#             # no_of_orders = request.data['no_of_orders']
#             # buying_capacity = request.data['buying_capacity']
#             # total_amount_shopped = request.data['total_amount_shopped']
#             # gender = request.data['gender']
#             # image = request.data['image']                        except:
#                             return Response(status=status.HTTP_400_BAD_REQUEST,
#                                             data="Error updating auth-user data")
#             # approval_status = request.data['approval_status']
#             try:
#                 # required parameters
#                 email = request.data['email']
#                 if email == "":
#                     return Response(status=status.HTTP_400_BAD_REQUEST,
#                                     data="Ooops! email can't be empty")
#                 try:
#                     saved_delivery_person = DeliveryPerson.objects.filter(email=email)
#                     if not saved_delivery_person:
#                         return Response(status=status.HTTP_404_NOT_FOUND,
#                                         data=f"delivery_person with email: '{email}' not found")
#                     try:
#                         updated_delivery_person = saved_delivery_person.update(
#                             first_name=first_name,
#                             last_name=last_name,
#                             phone_number=phone_number,
#                             address=address
#                             # current_location=current_location,
#                             # no_of_orders=no_of_orders,
#                             # buying_capacity=buying_capacity,
#                             # total_amount_shopped=total_amount_shopped,
#                             # gender=gender,
#                             # image=image,
#                             # approval_status=approval_status
#                         )
#                         try:
#                             saved_delivery_person.user.first_name = first_name
#                             saved_delivery_person.user.last_name = last_name
#                             serializer = DeliveryPersonSerializer(updated_delivery_person, many=True)
#                             return Response(status=status.HTTP_200_OK,
#                                             data={"updated_admin_user": serializer.data})
#                         except:
#                             return Response(status=status.HTTP_400_BAD_REQUEST,
#                                             data="Error updating auth-user data")
#                     except:
#                         return Response(status=status.HTTP_400_BAD_REQUEST,
#                                         data="Error updating admin_user Data")
#                 except:
#                     return Response(status=status.HTTP_404_NOT_FOUND,
#                                     data="Error finding auth user data")
#             except:
#                 return Response(status=status.HTTP_400_BAD_REQUEST,
#                                 data="Oops! Make sure you're not missing a required"
#                                      "field (email) ")
#         except:
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data="Oops! Make sure following fields are not missing "
#                                  "(first_name, last_name, phone_number, buying_capacity "
#                                  "address, gender, image) Note: If you want to "
#                                  "leave fields blank, then send null or empty"
#                                  "and for approval_status send either 'True' or 'False'")


class UpdateDeliveryPersonApiView(APIView):

    def put(self, request):
        try:
            saved_data = User.objects.get(email = request.data['email'])
            saved_data.first_name = request.data['first_name']
            saved_data.last_name = request.data['last_name']
            DeliveryPerson.objects.filter(user_id = saved_data.id).update(
                    first_name=request.data["first_name"],
                    last_name=request.data["last_name"],
                    phone_number=request.data["phone_number"],
                    address=request.data["address"]
                    # current_location=request.data["current_location"],
                    # gender=request.data["gender"],
                    # image=request.data["image"]
            )
            saved_data.save()
            data_to_pass = DeliveryPerson.objects.get(username=saved_data.username)
            serializer = DeliveryPersonSerializer(data_to_pass)
            return Response(status=status.HTTP_200_OK, data={"updated_details": serializer.data})
        except AssertionError as err:
            return Response(status=status.HTTP_404_NOT_FOUND, data=err)
# Delivery Person Delete API
class DeleteDeliveryPersonApiView(APIView):

    def get(self, request, id=None):
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        if id:
            try:
                saved_data = DeliveryPerson.objects.get(id=id)
                phone_number = saved_data.phone_number
                User.objects.get(id=saved_data.user.id).delete()
                twilio_verification = TwilioVerification(str(phone_number))
                twilio_verification.update_status()
                return Response(status=status.HTTP_200_OK,
                                data={'Record deleted against email': saved_data.username})
            except:
                return Response(status=status.HTTP_404_NOT_FOUND,
                                data="No Record Found!")
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"Error Msg": "ID missing from URL"})


class DeliveryPersonLogoUploadAPIView(APIView):
    serializer_class = DeliveryPersonSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    def get(self, request, id=None):
        if id:
            try:
                delivery_person = DeliveryPerson.objects.get(id=id)
                serializer_class = DeliveryPersonSerializer(delivery_person)

                return Response(status=status.HTTP_200_OK, data={"image": serializer_class.data['image']})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Delivery person not found'})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'ID not provided'})

    def post(self, request):
        # print(request.data['client_id'])
        serializer = DeliveryPersonImageSerializer(data=request.data)
        if serializer.is_valid():
            delivery_person = DeliveryPerson.objects.get(id=serializer.validated_data['id'])
            serializer.update(delivery_person, serializer.validated_data)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


# ------------------------------------------------------------------------------------------------------------------------


# CRUD operations of Business Detail
class BusinessDetailInsertApiView(APIView):

    def post(self, request):
        try:
            username = request.data['username']
            business_name = request.data['business_name']
            business_nature = request.data['business_nature']
            business_type = request.data['business_type']
            business_logo = request.data['business_logo']
            business_address = request.data['business_address']
            if username.strip() == "" or business_name.strip() == "" or business_nature.strip() == "" or business_type.strip() == "" or business_address.strip() == "":
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Do not leave fields empty.'})
            delivery_person = DeliveryPerson.objects.get(username=username)
            # count = 0
            # try:
            #     delivery_person_business = DeliveryPersonBusinessDetail.objects.get(delivery_person=delivery_person, name=business_name)
            #     # return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': f'Record with business name '
            #     #                                                                      f'{business_name} already '
            #     #                                                                      f'exists.'})
            #     print(delivery_person_business.name)
            #     count += 1
            # except Exception as e:
            #     print(e)

            try:
                delivery_person_business = DeliveryPersonBusinessDetail.objects.get(delivery_person=delivery_person, address=business_address)
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': f'Record with business address '
                                                                                     f'{business_address} already '
                                                                                     f'exists.'})
                # print(delivery_person_business.address)

                # count += 1 
            except Exception as e:
                print(e)

            # try:
            #     delivery_person_business = DeliveryPersonBusinessDetail.objects.get(delivery_person=delivery_person, nature=business_nature)
            #     # return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': f'Record with business nature '
            #     #                                                                      f'{business_nature} already '
            #     #                                                                      f'exists.'})
            #     print(delivery_person_business.nature)

            #     count += 1
            # except Exception as e:
            #     print(e)

            # try:
            #     delivery_person_business = DeliveryPersonBusinessDetail.objects.get(delivery_person=delivery_person, type=business_type)
            #     # return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': f'Record with business type '
            #     #                                                                      f'{business_type} already '
            #     #                                                                      f'exists.'})
            #     print(delivery_person_business.type)
            #     count += 1
            # except Exception as e:
            #     print(e)
            
            # print(count)
            # if count == 4:
            #     return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Record already exists'})

            business_detail = DeliveryPersonBusinessDetail.objects.create(
                delivery_person=delivery_person,
                name=business_name,
                address=business_address,
                nature=business_nature,
                type=business_type,
                logo=business_logo
            )
            bd = DeliveryPersonBusinessDetail.objects\
                .filter(id=business_detail.id, delivery_person=delivery_person)
            data_to_pass = DeliveryPersonBusinessDetailSerializer(bd, many=True)
            return Response(status=status.HTTP_200_OK,
                            data={"business_details": data_to_pass.data[0]})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"Exception": e})


class ListBusinessDetailsApiView(APIView):

    def get(self, request):
        if id:
            try:
                business_detail = DeliveryPersonBusinessDetail.objects.get(id=id)
                data_to_pass = DeliveryPersonBusinessDetailSerializer(business_detail)

            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={'Error': e})

        else:
            try:
                business_detail = DeliveryPersonBusinessDetail.objects.all()
                data_to_pass = DeliveryPersonBusinessDetailSerializer(business_detail, many=True)
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={'Error': e})

        return Response(status=status.HTTP_200_OK,
                        data={"business_details": data_to_pass.data})


class ListDeliveryPersonBusinessDetailsApiView(APIView):

    def get(self, request, id = None):
        if id:
            try:
                business_detail = DeliveryPersonBusinessDetail.objects.filter(delivery_person=id)
                data_to_pass = DeliveryPersonBusinessDetailSerializer(business_detail, many=True)
                return Response(status=status.HTTP_200_OK,
                                data={"delivery_person_businesses": data_to_pass.data})

            except Exception as e:
                return Response(status=status.HTTP_404_NOT_FOUND,
                                data={'Error' : 'delivery_person not found'})


class UpdateBusinessApiView(APIView):

    def put(self, request):
        try:
            business_id = request.data['id']
            business_name = request.data['business_name']
            business_nature = request.data['business_nature']
            business_type = request.data['business_type']
            business_logo = request.data['business_logo']
            business_address = request.data['business_address']

            # count = 0
            # try:
            #     DeliveryPersonBusinessDetail.objects.get(delivery_person=delivery_person, name=business_name)
            #     # return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': f'Record with business name '
            #     #                                                                      f'{business_name} already '
            #     #                                                                      f'exists.'})
            #     count += 1
            # except:
            #     pass

            # try:
            #     DeliveryPersonBusinessDetail.objects.get(delivery_person=delivery_person, address=business_address)
            #     return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': f'Record with business address '
            #                                                                          f'{business_address} already '
            #                                                                          f'exists.'})
            #     # count += 1 
            # except:
            #     pass

            # try:
            #     DeliveryPersonBusinessDetail.objects.get(delivery_person=delivery_person, nature=business_nature)
            #     # return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': f'Record with business nature '
            #     #                                                                      f'{business_nature} already '
            #     #                                                                      f'exists.'})
            #     count += 1
            # except:
            #     pass

            # try:
            #     DeliveryPersonBusinessDetail.objects.get(delivery_person=delivery_person, type=business_type)
            #     # return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': f'Record with business type '
            #     #                                                                      f'{business_type} already '
            #     #                                                                      f'exists.'})
            #     count += 1
            # except:
            #     pass
            
            # if count == 4:
            #     return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Record already exists'})

            business_detail = DeliveryPersonBusinessDetail.objects.filter(id=business_id).update(
                name=business_name,
                nature=business_nature,
                address=business_address,
                type=business_type,
                logo=business_logo
            )
            print("Business Detail id :", business_detail)
            bd = DeliveryPersonBusinessDetail.objects.get(id=business_id)
            data_to_pass = DeliveryPersonBusinessDetailSerializer(bd)
            return Response(status=status.HTTP_200_OK,
                            data={"updated_business_details": data_to_pass.data})

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"Exception": e})


class DeleteBusinessApiView(APIView):

    def delete(self, request, id=None):
        if id:
            try:
                business = DeliveryPersonBusinessDetail.objects.get(id=id).delete()
                name = business.name
                return Response(status=status.HTTP_200_OK,
                                data={"business_delete": name})

            except Exception as e:
                return Response(status=status.HTTP_404_NOT_FOUND,
                                data={"error": "record not found against the given id"})


# ------------------------------------------------------------------------------------------------------------------------


class BankDetailsCreate(generics.CreateAPIView):
    serializer_class = DeliveryPersonBankDetailSerializer
    queryset = DeliveryPersonBankDetail.objects.all()


class BankDetailsUpdate(generics.UpdateAPIView):
    serializer_class = DeliveryPersonBankDetailSerializer
    queryset = DeliveryPersonBankDetail.objects.all()

class ListBankDetailsApiView(APIView):
    def get(self, request, id=None):
            if id:
                try:
                    bank_detail = DeliveryPersonBankDetail.objects.get(id=id)
                    data_to_pass = DeliveryPersonBankDetailSerializer(bank_detail)

                except Exception as e:
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data={'Error': e})

            else:
                try:
                    bank_details = DeliveryPersonBankDetail.objects.all()
                    data_to_pass = DeliveryPersonBankDetailSerializer(bank_details, many=True)
                except Exception as e:
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data={'Error': e})

            return Response(status=status.HTTP_200_OK,
                            data={"bank_details": data_to_pass.data})


class ListDeliveryPersonBankDetailsApiView(APIView):

    def get(self, request, id=None):
        if id:
            try:
                bank_details = DeliveryPersonBankDetail.objects.filter(delivery_person__id=id)
                data_to_pass = DeliveryPersonBankDetailSerializer(bank_details, many=True)
                return Response(status=status.HTTP_200_OK,
                                data={"bank_details": data_to_pass.data})

            except Exception as e:
                return Response(status=status.HTTP_404_NOT_FOUND,
                                data={'Error': 'Delivery Person not found'})


class DeleteBankDetailsApiView(APIView):

    def delete(self, request, id=None):
        if id:
            try:
                bank_rec = DeliveryPersonBankDetail.objects.get(id=id)
                bank_name = bank_rec.bank_name
                bank_rec.delete()
                return Response(status=status.HTTP_200_OK,
                                data={"record_deleted": bank_name})

            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"Error": "Unable to delete record"})


# ------------------------------------------------------------------------------------------------------------------------

class PackageCreate(generics.CreateAPIView):
    serializer_class = DeliveryPersonPackageSerializer
    queryset = DeliveryPersonPackage.objects.all()


class RetrieveUpdateDestroyPackage(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeliveryPersonPackageSerializer
    queryset = DeliveryPersonPackage.objects.all()
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        print('here')
        queryset = self.get_queryset()
        pk = self.kwargs.get('id')
        if pk:
            delivery_person_package = get_object_or_404(queryset, pk=pk)
            serializer = DeliveryPersonPackageSerializer(delivery_person_package)
            return Response(serializer.data)
        else:
            serializer = DeliveryPersonPackageSerializer(queryset, many=True)
            return Response(serializer.data)


# create package
class PackageCreateApiView(APIView):

    def post(self, request):
        name = request.data['name']
        try:
            package = DeliveryPersonPackage.objects.get(name=name)
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"error": f"{name} record already exists"})
        except:
            try:
                description = request.data['description']
                price = request.data['price']
                package_record = DeliveryPersonPackage.objects.create(
                    name=name,
                    description=description,
                    price=price
                )
                data_to_pass = DeliveryPersonPackageSerializer(package_record)
                return Response(status=status.HTTP_200_OK,
                                data={"package_created": data_to_pass.data})
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"Exception": e})


# Update package
class PackageUpdateApiView(APIView):

    def put(self, request):
        try:
            name = request.data['name']
            package = DeliveryPersonPackage.objects.get(name=name)
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"error": f"{package.name} record already exists"})
        except:
            try:
                package_id = request.data['id']
                name = request.data['name']
                description = request.data['description']
                price = request.data['price']

                package_detail = DeliveryPersonPackage.objects.filter(id=package_id).update(
                    name=name,
                    description=description,
                    price=price,
                )
                print("Package ID :", package_detail)
                bd = DeliveryPersonPackage.objects.get(id=package_id)
                data_to_pass = DeliveryPersonPackageSerializer(bd)
                return Response(status=status.HTTP_200_OK,
                                data={"updated_package": data_to_pass.data})

            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"Exception": e})


# Get all packages
class ListPackagesApiView(APIView):

    def get(self, request, id=None):
        if id:
            try:
                package = DeliveryPersonPackage.objects.filter(id=id)
                data_to_pass = DeliveryPersonPackageSerializer(package, many=True)
                return Response(status=status.HTTP_200_OK,
                                data={"package_details": data_to_pass.data})

            except Exception as e:
                return Response(status=status.HTTP_404_NOT_FOUND,
                                data={'Error': 'package not found'})
        else:
            try:
                package = DeliveryPersonPackage.objects.all().order_by('id')
                data_to_pass = DeliveryPersonPackageSerializer(package, many=True)
                return Response(status=status.HTTP_200_OK,
                                data={"all_package": data_to_pass.data})

            except Exception as e:
                return Response(status=status.HTTP_404_NOT_FOUND,
                                data={'Error': 'package not found'})


class ListDeliveryPersonPackagesApiView(APIView):

    def get(self, request):
        if id:
            try:
                delivery_person_in_package = DeliveryPerson.objects.filter(package__id=id)
                data_to_pass = DeliveryPersonSerializer(delivery_person_in_package, many=True)
                return Response(status=status.HTTP_200_OK,
                                data={"delivery_person_in_package": data_to_pass.data})

            except Exception as e:
                return Response(status=status.HTTP_404_NOT_FOUND,
                                data={'Error': 'package not found'})


class DeletePackageApiView(APIView):

    def delete(self, request, id=None):
        if id:
            try:
                package_rec = DeliveryPersonPackage.objects.get(id=id)
                package_name = package_rec.name
                package_rec.delete()
                return Response(status=status.HTTP_200_OK,
                                data={"record_deleted": package_name})

            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"Error": "Unable to delete record"})


# ------------------------------------------------------------------------------------------------------------------------


# Update delivery person approval status
class UpdateDeliveryPersonApprovalStatus(APIView):

    def post(self, request):
        try:
            # required parameters
            delivery_person_id = request.data['delivery_person']
            admin_id = request.data['admin']
            admin_approval_status = request.data['admin_approval_status']
            if delivery_person_id == "" \
                    and admin_id == "" \
                    and admin_approval_status == "":
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "id of delivery_person, admin or "
                                      "admin_approval_status can't be empty"})
            try:
                delivery_person = DeliveryPerson.objects.get(id=delivery_person_id)
                admin = AdminUser.objects.get(id=admin_id)
                if not admin_approval_status == 'approved' \
                        and not admin_approval_status == 'unapproved' \
                        and not admin_approval_status == 'pending' \
                        and not admin_approval_status == 'cancelled':
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data={"message": "incorrect option for approval status"})
                try:
                    new_approval_log = DeliveryPersonApprovalLog.objects.create(
                        delivery_person=delivery_person,
                        admin=admin,
                        admin_approval_status=admin_approval_status
                    )
                    serializer = DeliveryPersonApprovalLogSerializer(new_approval_log)
                    delivery_person.admin_approval_status = admin_approval_status
                    delivery_person.save()
                    try:
                        send_mail(
                            'Notification Email',
                            f'Your account is {admin_approval_status}.',
                            'orddel@viltco.com',
                            [f"{delivery_person.email}"],
                            fail_silently=False,
                        )
                    except:
                        return Response(status=status.HTTP_200_OK,
                                        data={"status": f"log created {serializer.data}"
                                                        f"but email can not be sent, possibly due"
                                                        f"to wrong email address provided "
                                                        f"on registration"})
                    return Response(status=status.HTTP_200_OK,
                                    data={"log_created": serializer.data})
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data={"message": "Error creating client approval log"})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "invalid client or admin ID"})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"message": "missing one or more required"
                                             "fields (id of client, admin and admin_approval_status) "})


# ------------------------------------------------------------------------------------------------------------------------


class PendingApprovalListApiView(APIView):

    def get(self, request):
        try:
            admin_approval_status = self.request.query_params.get('admin_approval_status').lower()
            try:
                delivery_person = DeliveryPerson.objects.filter(admin_approval_status=admin_approval_status)
                serializer = DeliveryPersonSerializer(delivery_person, many=True)
                if not delivery_person:
                    return Response(status=status.HTTP_200_OK,
                                    data={"message": "Delivery Person table is empty"})
                return Response(status=status.HTTP_200_OK,
                                data={"pending_approval_list": serializer.data})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            pass


# ------------------------------------------------------------------------------------------------------------------------
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        return data


# ------------------------------------------------------------------------------------------------------------------------

class DeliveryPersonLogin(TokenObtainPairView):

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
                user = User.objects.get(username=username)
                delivery_person = DeliveryPerson.objects.get(username=username)
                is_active = user.is_active
                otp_status = delivery_person.otp_status
                approval_status = delivery_person.admin_approval_status
                print(is_active)
                print(otp_status)
                print(approval_status)
                if is_active and otp_status and approval_status == 'approved':
                    return Response(status=status.HTTP_200_OK, data={"delivery_person": delivery_person.id, "data": serializer_class.validated_data})
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED, data={"message": "The user is not authorized"})

            else:
                print("invalid username and password")

        except:
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

# Order notification
class UpdateDeliveryPersonOrderApiView(APIView):

    def post(self, request):
        try:
            order_id = request.data['order_id']
            delivery_person_action = request.data['delivery_person_action'].lower()
            order_detail = OrderDetail.objects.get(id=order_id)
            if delivery_person_action == "accepted":
                # Create Accepted Order Entry in Delivery Person
                delivery_person = order_detail.delivery_person
                delivery_person_obj = DeliveryPerson.objects.get(id=delivery_person.id)
                delivery_person_package = DeliveryPersonPackageLog.objects.filter(delivery_person=delivery_person_obj).last()

                if delivery_person_package:
                    if delivery_person_package.date_expiry <= date.today():
                        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Your package has been expired '
                                                                                                'Kindly renew it to use our '
                                                                                                'services'})
                    else:
                        pass

                if delivery_person_obj.no_of_invoices != 0 and delivery_person_obj.no_of_invoices != -1:
                    delivery_person_obj.no_of_invoices -= 1
                
                elif delivery_person_obj.no_of_invoices != -1:
                    return Response(status=status.HTTP_401_UNAUTHORIZED, data={'message': 'Cant accept, Invoices are empty'})
                
                delivery_person_obj.used_invoices += 1
                delivery_person_obj.save()

                order_detail.status = 'in_progress'
                user_id = order_detail.order_box.client.user.id
                try:
                    device = FCMDevice.objects.filter(user=user_id, active=True)
                    device.send_message(title="Order Accepted", body="Your order has been accepted.")
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Unable to send notification'})

            elif delivery_person_action == "rejected":
                # transfer order to other delivery person
                order_detail.status = 'rejected'
                user_id = order_detail.order_box.client.user.id
                try:
                    device = FCMDevice.objects.filter(user=user_id, active=True)
                    device.send_message(title="Order Rejected", body="Your order has been rejected.")
                
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Unable to send notification'})

            elif delivery_person_action == "purchased":
                order_detail.status = 'purchased'

            elif delivery_person_action == "pending":
                order_detail.status = 'pending'

            elif delivery_person_action == "delivered":
                order_detail.status = 'delivered'
                user_id = order_detail.order_box.client.user.id
                try:
                    device = FCMDevice.objects.filter(user=user_id)
                    device.send_message(title="Order Delivered", body="Your order has been delivered.")
                
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Unable to send notification'})


            else:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={
                                    "status": "HTTP_400_BAD_REQUEST",
                                    "message": "Unsuccessful",
                                    "detail": "Wrong choice entered for update order status",
                                    "action": delivery_person_action

                                })
            order_detail.save()

            return Response(status=status.HTTP_200_OK,
                            data={
                                "status": "HTTP_200_OK",
                                "message": "Successful",
                                "action": delivery_person_action

                            })
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={
                                "status": "HTTP_400_BAD_REQUEST",
                                "message": "Unsuccessful",
                                "details": "Something went wrong, please check the data entered"
        
                            })

# ------------------------------------------------------------------------------------------------------------------------
