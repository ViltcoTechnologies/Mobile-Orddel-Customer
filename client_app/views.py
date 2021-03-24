from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt import authentication
from django_email_verification import sendConfirm
from rest_framework.response import Response
import datetime
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from client_app.models import *
from order.models import *
from admin_dashboard.models import *
from .serializers import *
from admin_dashboard.serializers import *
import json
from django.core.mail import send_mail
from ordel.verificaton import TwilioVerification

# Token Obtain pair
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from axes.backends import AxesBackend as a
from rest_framework_simplejwt.authentication import JWTAuthentication


# Client home screen Dashboard
class ClientDashboardApiView(APIView):

    def get(self, request, id=None):
        try:
            client_id = id
            if client_id == "":
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "client can't be empty"})
            try:
                client = Client.objects.get(id=client_id)
                try:
                    client_image = client.image
                    client_name = f"{client.first_name} {client.last_name}"
                    client_package = client.package.name
                    total_invoices = client.package.no_of_invoices
                    preferred_delivery_person = client.preferred_delivery_person
                    print(preferred_delivery_person.first_name)
                    preferred_delivery_person_name = f"{preferred_delivery_person.first_name} {preferred_delivery_person.last_name}"
                    preferred_delivery_person_address = client.preferred_delivery_person.address
                    print(preferred_delivery_person_address)
                    remaining_invoices = client.no_of_invoices
                    # used_invoices = total_invoices - remaining_invoices
                    used_invoices = client.used_invoices
                    no_of_pending_orders = OrderDetail.objects.filter(status="pending", order_box__client=client_id)
                    no_of_completed_orders = OrderDetail.objects.filter(status="delivered", order_box__client=client_id)
                    no_of_in_progress_orders = OrderDetail.objects.filter(status="in_progress", order_box__client=client_id)
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
                        # "client_image": client_image,
                        "client_name": client_name,
                        "client_first_name": client.first_name, 
                        "client_last_name": client.last_name, 
                        "client_phone": client.phone_number,
                        "client_user_name": client.username, 
                        "client_package": client_package.capitalize(),
                        "total_invoices": total_invoices,
                        "remaining_invoices": remaining_invoices,
                        "used_invoices": used_invoices,
                        "no_of_pending_orders": no_of_pending_orders,
                        "no_of_completed_orders": no_of_completed_orders,
                        "no_of_in_progress_orders": no_of_in_progress_orders,
                        "preferred_delivery_person": preferred_delivery_person.id,
                        "preferred_delivery_person_name": preferred_delivery_person_name,
                        "preferred_delivery_person_address": preferred_delivery_person_address
                    }
                    return Response(status=status.HTTP_200_OK,
                                    data={"client_dashboard": data})
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data={"message": "There was a error fetching data "
                                                    "from the database"})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "Incorrect Client ID"})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"message": "client is required"})


# CRUD operations of client
class ClientRegisterApiView(APIView):
    def post(self, request):
        try:
            # optional parameters
            current_location = request.data['current_location']
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
                admin_approval_status = 'pending'
                package = request.data['package']
                preferred_delivery_person = request.data['preferred_delivery_person']

                if first_name == ""\
                        or last_name == ""\
                        or email == ""\
                        or phone_number == ""\
                        or password == "":
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data={"message": "following required fields can't "
                                          "be empty: (first_name, last_name, email, "
                                          "phone_number, password)"})
                try:
                    saved_data = Client.objects.get(phone_number=phone_number)
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data={"message": "Phone Number already registered!"})
                except:
                        try:
                            package = ClientPackage.objects.get(id=package)
                            no_of_invoices = package.no_of_invoices
                            try:
                                new_auth_user = User.objects.create_user(
                                    email,
                                    email,
                                    password
                                )
                                new_auth_user.first_name = first_name
                                new_auth_user.last_name = last_name

                                try:
                                    try:
                                        delivery_person = DeliveryPerson.objects.get(id=preferred_delivery_person)
                                    except:
                                        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Delivery Person does not exist'})
                                    new_client = Client.objects.create(
                                        user=new_auth_user,
                                        preferred_delivery_person=delivery_person,
                                        package=package,
                                        first_name=first_name,
                                        last_name=last_name,
                                        username=username,
                                        admin_approval_status=admin_approval_status,
                                        email=email,
                                        no_of_invoices=no_of_invoices,
                                        current_location=current_location,
                                        phone_number=phone_number,
                                        address=address,
                                        gender=gender,
                                        image=image
                                    )
                                    # Create Initial Package Log

                                    try:
                                        twilio_verification = TwilioVerification(str(phone_number))
                                        twilio_verification.send_otp()
                                        try:
                                            sendConfirm(new_auth_user)
                                        except:
                                            return Response(status=status.HTTP_400_BAD_REQUEST,
                                                            data={"message": "There was a error sending verification "
                                                                             "email"})
                                    except:
                                        return Response(status=status.HTTP_400_BAD_REQUEST,
                                                        data={"message": "There was a error sending otp "
                                                                         "please try to sign up again"})
                                    new_client.save()
                                    serializer = ClientSerializer(new_client)
                                    new_auth_user.save()

                                    return Response(status=status.HTTP_200_OK,
                                                    data={"client_created": serializer.data})
                                except:
                                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                                    data={"message": "there was a error creating "
                                                                     "client "})
                            except:
                                return Response(status=status.HTTP_400_BAD_REQUEST,
                                                data={"message": "User already exists"})
                        except:
                            return Response(status=status.HTTP_404_NOT_FOUND,
                                            data={"message": f"No package with the ID: {package}"})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "Error! Make sure you're not missing one of the "
                                      "following required fields: (first_name, last_name, "
                                      "email, phone_number, password)"})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={"message": "Make sure you're not missing one "
                                  "of the following optional fields: "
                                  "(current_location, address, gender, image) "
                                  "Note: If you want to leave fields blank, then "
                                  "send null or empty"})


class ClientRegisterV2ApiView(APIView):
    def post(self, request):
        try:
            # optional parameters
            current_location = request.data['current_location']
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
                otp_status = request.data['otp_status']
                admin_approval_status = 'pending'
                package = request.data['package']
                preferred_delivery_person = request.data['preferred_delivery_person']

                if first_name == ""\
                        or last_name == ""\
                        or email == ""\
                        or phone_number == ""\
                        or otp_status == ""\
                        or password == "":
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data={"message": "following required fields can't "
                                          "be empty: (first_name, last_name, email, otp_status"
                                          "phone_number, password)"})
                try:
                    saved_data = Client.objects.get(phone_number=phone_number)
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data={"message": "Phone Number already registered!"})
                except:
                        try:
                            package = ClientPackage.objects.get(id=package)
                            no_of_invoices = package.no_of_invoices
                            try:
                                new_auth_user = User.objects.create_user(
                                    email,
                                    email,
                                    password
                                )
                                new_auth_user.first_name = first_name
                                new_auth_user.last_name = last_name
                                try:
                                    delivery_person = DeliveryPerson.objects.get(id=preferred_delivery_person)
                                except:
                                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                                    data={'error': 'Delivery Person does not exist'})

                                try:
                                    new_client = Client.objects.create(
                                        user=new_auth_user,
                                        preferred_delivery_person=delivery_person,
                                        package=package,
                                        otp_status=otp_status,
                                        first_name=first_name,
                                        last_name=last_name,
                                        username=username,
                                        admin_approval_status=admin_approval_status,
                                        email=email,
                                        no_of_invoices=no_of_invoices,
                                        current_location=current_location,
                                        phone_number=phone_number,
                                        address=address,
                                        gender=gender,
                                        image=image
                                    )
                                    try:
                                        ClientPackageLog.objects.create(
                                            client=new_client,
                                            package=package,
                                            date_expiry=datetime.datetime.now() + datetime.timedelta(
                                                package.validity_in_days),
                                            status='active'

                                        )
                                    except:
                                        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Unable to create Client '
                                                                                                             'Package Log'})
                                    try:
                                        sendConfirm(new_auth_user)
                                    except:
                                        return Response(status=status.HTTP_400_BAD_REQUEST,
                                                        data={"message": "There was a error sending verification "
                                                                             "email"})

                                    new_client.save()
                                    serializer = ClientSerializer(new_client)
                                    new_auth_user.save()


                                    return Response(status=status.HTTP_200_OK,
                                                    data={"client_created": serializer.data})
                                except:
                                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                                    data={"message": "there was a error creating "
                                                                     "delivery_person was not created"})
                            except:
                                return Response(status=status.HTTP_400_BAD_REQUEST,
                                                data={"message": "User already exists"})
                        except:
                            return Response(status=status.HTTP_404_NOT_FOUND,
                                            data={"message": f"No package with the ID: {package}"})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "Error! Make sure you're not missing one of the "
                                      "following required fields: (first_name, last_name, otp_status"
                                      "email, phone_number, password)"})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={"message": "Make sure you're not missing one "
                                  "of the following optional fields: "
                                  "(current_location, address, gender, image) "
                                  "Note: If you want to leave fields blank, then "
                                  "send null or empty"})


class UpdateClientApiView(APIView):

    def put(self, request):
        try:
            saved_data = User.objects.get(email = request.data['email'])
            saved_data.first_name = request.data['first_name']
            saved_data.last_name = request.data['last_name']
            Client.objects.filter(user_id = saved_data.id).update(
                    first_name=request.data["first_name"],
                    last_name=request.data["last_name"],
                    phone_number=request.data["phone_number"]
                    # address=request.data["address"],
                    # current_location=request.data["current_location"],
                    # gender=request.data["gender"],
                    # image=request.data["image"]
            )
            saved_data.save()
            data_to_pass = Client.objects.get(username=saved_data.username)
            serializer = ClientSerializer(data_to_pass)
            return Response(status=status.HTTP_200_OK, data={"updated_details": serializer.data})
        except AssertionError as err:
            return Response(status=status.HTTP_404_NOT_FOUND, data=err)


class DeleteClientApiView(APIView):

    def delete(self, request, id=None):
        if id:
            try:
                client = Client.objects.get(id=id)
                user = User.objects.get(id=client.user.id)
                username = user.username
                user.delete()
                return Response(status=status.HTTP_200_OK, data={"Deleted record against username": username})
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"Exception": e})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Error Msg": "ID missing from URL"})


class ListClientsApiView(APIView):

    def get(self, request, id=None):
        try:
            if id:
                clients = Client.objects.get(id=id)
                data_to_pass = ClientSerializer(clients)
            else:
                clients = Client.objects.all().order_by('-date_created')
                data_to_pass = ClientSerializer(clients, many=True)
            return Response(status=status.HTTP_200_OK, data={"client": data_to_pass.data})
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"No Clients Found"})


class ClientLogoUploadAPIView(APIView):
    serializer_class = ClientSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    def get(self, request, id=None):
        if id:
            client = Client.objects.get(id=id)
            serializer_class = ClientSerializer(client)

            return Response(status=status.HTTP_200_OK, data={"image": serializer_class.data['image']})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        # print(request.data['client_id'])
        print(request.data['image'])
        serializer = ClientImageSerializer(data=request.data)
        if serializer.is_valid():
            client = Client.objects.get(id=serializer.validated_data['id'])
            # print(serializer.validated_data['image'])
            serializer.update(client, serializer.validated_data)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CRUD operations of Business Detail
class BusinessDetailInsertApiView(APIView):

    def post(self, request):
        try:
            client_id = request.data['client']
            business_name = request.data['name']
            business_address = request.data['address']
            business_nature = request.data['nature']
            business_type = request.data['type']
            business_logo = request.data['logo']
            try:
                client = Client.objects.get(id=client_id)
                business_detail = ClientBusinessDetail.objects.create(
                    client=client,
                    name=business_name,
                    address=business_address,
                    nature=business_nature,
                    type=business_type,
                    logo=business_logo
                )
                print(business_detail.id)
                bd = ClientBusinessDetail.objects.filter(id=business_detail.id, client=client)
                data_to_pass = BusinessDetailSerializer(bd, many=True)
                return Response(status=status.HTTP_200_OK,
                                data={"business_details": data_to_pass.data[0]})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data="There was a error inserting business details")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"message": "you're missing on the required fields"})


class ListBusinessDetailsApiView(APIView):

    def get(self, request, id=None):
        if id:
            try:
                business_detail = ClientBusinessDetail.objects.get(id=id)
                data_to_pass = BusinessDetailSerializer(business_detail)

            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'Error': e})

        else:
            try:
                business_detail = ClientBusinessDetail.objects.all()
                data_to_pass = BusinessDetailSerializer(business_detail, many=True)
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'Error': e})

        return Response(status=status.HTTP_200_OK, data={"business_details": data_to_pass.data})


class ListClientBusinessDetailsApiView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                business_detail = ClientBusinessDetail.objects.filter(client__id=id)
                data_to_pass = BusinessDetailSerializer(business_detail, many=True)
                return Response(status=status.HTTP_200_OK, data={"client_businesses": data_to_pass.data})

            except Exception as e:
                return Response(status=status.HTTP_404_NOT_FOUND, data={'Error': 'client or business not found'})


class UpdateBusinessApiView(APIView):

    def put(self, request, id=None):
        try:
            business_id = request.data['id']
            business_name = request.data['business_name']
            business_nature = request.data['business_nature']
            business_type = request.data['business_type']
            business_address = request.data['address']
            # business_logo = request.data['business_logo']

            business_detail = ClientBusinessDetail.objects.filter(id=business_id).update(
                name=business_name,
                nature=business_nature,
                type=business_type,
                address=business_address
                # logo=business_logo
            )
            print("Business Detail id :", business_detail)
            bd = ClientBusinessDetail.objects.get(id=business_id)
            data_to_pass = BusinessDetailSerializer(bd)
            return Response(status=status.HTTP_200_OK, data={"updated_business_details": data_to_pass.data})

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Exception": e})


class DeleteBusinessApiView(APIView):

    def delete(self, request, id = None):
        if id:
            try:
                business = ClientBusinessDetail.objects.get(id=id).delete()
                name = business.name
                return Response(status = status.HTTP_200_OK, data={"business_delete": name})

            except Exception as e:
                return Response(status=status.HTTP_404_NOT_FOUND,
                                data={"error": "record not found against the given id"})


# ----------------------------------------------------------------------------------------------------------------
# Business Details API v2
class BusinessDetailInsertGeneric(generics.ListCreateAPIView):
    queryset = ClientBusinessDetail.objects.all()
    lookup_field = 'client'
    serializer_class = BusinessDetailSerializer


# CRUD of Shipment Address

class ShipmentAddressCreateApiView(APIView):

    def post(self, request):
        client_id = request.data['client_id']
        shipment_address = request.data['shipment_address']

        client = Client.objects.get(id=client_id)
        shipment_record = ClientShipmentAddress.objects.create(
            client=client,
            shipment_address=shipment_address
        )
        # shipment = ShipmentAddress.objects.get(id = shipment_record.id)
        data_to_pass = ShipmentAddressSerializer(shipment_record)
        return Response(status = status.HTTP_200_OK, data={"shipment_address_created": data_to_pass.data})


class ListShipmentAddressApiView(APIView):

    def get(self, request):
        if id:
            try:
                shipment_address = ClientShipmentAddress.objects.get(id=id)
                data_to_pass = ShipmentAddressSerializer(shipment_address)

            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'Error': e})

        else:
            try:
                shipment_address = ClientShipmentAddress.objects.all()
                data_to_pass = ShipmentAddressSerializer(shipment_address, many=True)
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'Error': e})

        return Response(status=status.HTTP_200_OK, data={"shipment_addresses": data_to_pass.data})


class ListClientShipmentAddressApiView(APIView):

    def get(self, request):
        if id:
            try:
                shipment = ClientShipmentAddress.objects.filter(client__id=id)
                data_to_pass = ShipmentAddressSerializer(shipment, many=True)
                return Response(status=status.HTTP_200_OK, data={"client_shipment_addresses": data_to_pass.data})

            except Exception as e:
                return Response(status = status.HTTP_404_NOT_FOUND, data={'Error' : 'client not found'})


class UpdateShipmentAddressApiView(APIView):

    def put(self, request):
        try:
            shipment_id = request.data['shipment_id']
            shipment_address = request.data['shipment_address']

            shipment_rec = ClientShipmentAddress.objects.filter(id=shipment_id)
            shipment_rec.update(
                id=shipment_id,
                shipment_address=shipment_address
            )
            print(shipment_rec)
            data_to_pass = ShipmentAddressSerializer(shipment_rec, many=True)
            return Response(status=status.HTTP_200_OK, data={"updated_business_details": data_to_pass.data})

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Exception": e})


class DeleteShipmentAddressApiView(APIView):

    def delete(self, request):
        if id:
            try:
                shipment_rec = ClientShipmentAddress.objects.get(id=id)
                address = shipment_rec.shipment_address
                shipment_rec.delete()
                return Response(status=status.HTTP_200_OK, data={"record_deleted": address})

            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"Error": "Unable to delete record"})


class BankDetailsCreateApiView(APIView):
    def post(self, request):
        try:
            client_id = request.data['client_id']
            bank_name = request.data['bank_name']
            branch_code = request.data['branch_code']
            credit_card_no = request.data['credit_card_no']
            sort_code = request.data['sort_code']
            credit_card_expiry = request.data['credit_card_expiry']

            client = Client.objects.get(id = client_id)
            bank_record = ClientBankDetail.objects.create(
                client=client,
                bank_name=bank_name,
                branch_code=branch_code,
                credit_card_no=credit_card_no,
                sort_code=sort_code,
                credit_card_expiry=credit_card_expiry
            )
            data_to_pass = BankDetailsSerializer(bank_record)
            return Response(status=status.HTTP_200_OK, data={"bank_details_created": data_to_pass.data})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Exception" : e})


class BankDetailsUpdateApiView(APIView):
    def put(self, request):
        try:
            bank_detail_id = request.data['id']
            bank_name = request.data['bank_name']
            branch_code = request.data['branch_code']
            credit_card_no = request.data['credit_card_no']
            sort_code = request.data['sort_code']
            credit_card_expiry = request.data['credit_card_expiry']

            bank_detail = ClientBankDetail.objects.filter(id=bank_detail_id).update(
                bank_name=bank_name,
                branch_code=branch_code,
                credit_card_no=credit_card_no,
                sort_code=sort_code,
                credit_card_expiry=credit_card_expiry
            )
            print("Bank Detail id :", bank_detail)
            bd = ClientBankDetail.objects.get(id=bank_detail_id)
            data_to_pass = BankDetailsSerializer(bd)
            return Response(status=status.HTTP_200_OK, data={"updated_business_details": data_to_pass.data})

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Exception": e})


class ListBankDetailsApiView(APIView):
    def get(self, request, id=None):
            if id:
                try:
                    bank_detail = ClientBankDetail.objects.get(id=id)
                    data_to_pass = BankDetailsSerializer(bank_detail)

                except Exception as e:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'Error': e})

            else:
                try:
                    bank_details = ClientBankDetail.objects.all()
                    data_to_pass = BankDetailsSerializer(bank_details, many=True)
                except Exception as e:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'Error': e})

            return Response(status=status.HTTP_200_OK, data={"bank_details": data_to_pass.data})


class ListClientBankDetailsApiView(APIView):

    def get(self, request):
        if id:
            try:
                bank_details = ClientBankDetail.objects.filter(client__id=id)
                data_to_pass = BankDetailsSerializer(bank_details, many=True)
                return Response(status=status.HTTP_200_OK, data={"bank_details": data_to_pass.data})

            except Exception as e:
                return Response(status=status.HTTP_404_NOT_FOUND, data={'Error': 'client not found'})


class DeleteBankDetailsApiView(APIView):

    def delete(self, request, id = None):
        if id:
            try:
                bank_rec = ClientBankDetail.objects.get(id = id)
                bank_name = bank_rec.bank_name
                bank_rec.delete()
                return Response(status = status.HTTP_200_OK, data={"record_deleted": bank_name})

            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"Error": "Unable to delete record"})


class PackageCreateApiView(APIView):
    def post(self, request):
        name = request.data['name']
        try:
            package = ClientPackage.objects.get(name=name)
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": f"{name} record already exists"})

        except:
            try:

                description = request.data['description']
                price = request.data['price']
                package_record = ClientPackage.objects.create(
                    name=name,
                    description=description,
                    price=price

                )
                data_to_pass = PackageSerializer(package_record)
                return Response(status=status.HTTP_200_OK, data={"package_created": data_to_pass.data})
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"Exception": e})


class PackageUpdateApiView(APIView):
    def put(self, request):
        try:
            name = request.data['name']
            package = ClientPackage.objects.get(name=name)
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": f"{package.name} record already exists"})

        except:
            try:
                package_id = request.data['id']
                name = request.data['name']
                description = request.data['description']
                price = request.data['price']

                package_detail = ClientPackage.objects.filter(id=package_id).update(
                    name=name,
                    description=description,
                    price=price,

                )
                print("Package ID :", package_detail)
                bd = ClientPackage.objects.get(id=package_id)
                data_to_pass = PackageSerializer(bd)
                return Response(status=status.HTTP_200_OK, data={"updated_business_details": data_to_pass.data})

            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"Exception": e})


class ListPackagesApiView(APIView):
    def get(self, request):
        if id:
            try:
                package = ClientPackage.objects.filter(id=id)
                data_to_pass = PackageSerializer(package, many=True)
                return Response(status=status.HTTP_200_OK, data={"package_details": data_to_pass.data})

            except Exception as e:
                return Response(status=status.HTTP_404_NOT_FOUND, data={'Error': 'package not found'})
        else:
            try:
                package = ClientPackage.objects.all()
                data_to_pass = PackageSerializer(package, many=True)
                return Response(status=status.HTTP_200_OK, data={"all_package": data_to_pass.data})

            except Exception as e:
                return Response(status=status.HTTP_404_NOT_FOUND, data={'Error': 'package not found'})


class ListClientPackagesApiView(APIView):
    def get(self, request):
        if id:
            try:
                clients_in_package = Client.objects.filter(package__id=id)
                data_to_pass = ClientSerializer(clients_in_package, many=True)
                return Response(status=status.HTTP_200_OK, data={"clients_in_package": data_to_pass.data})

            except Exception as e:
                return Response(status=status.HTTP_404_NOT_FOUND, data={'Error': 'package not found'})


class DeletePackageApiView(APIView):
    def delete(self, request, id=None):
        if id:
            try:
                package_rec = ClientPackage.objects.get(id=id)
                package_name = package_rec.name
                package_rec.delete()
                return Response(status=status.HTTP_200_OK, data={"record_deleted": package_name})

            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"Error": "Unable to delete record"})


# ------------------------------------------------------------------------------------------------------------------------


# Update client approval status
class UpdateClientApprovalStatus(APIView):

    def post(self, request):
        try:
            # required parameters
            client_id = request.data['client']
            admin_id = request.data['admin']
            admin_approval_status = request.data['admin_approval_status']
            if client_id == "" \
                    and admin_id == "" \
                    and admin_approval_status == "":
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "id of client, admin or "
                                      "admin_approval_status can't be empty"})
            try:
                client = Client.objects.get(id=client_id)
                admin = AdminUser.objects.get(id=admin_id)
                if not admin_approval_status == 'approved' \
                        and not admin_approval_status == 'unapproved' \
                        and not admin_approval_status == 'pending' \
                        and not admin_approval_status == 'cancelled':
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data={"message": "incorrect option for approval status"})
                try:
                    new_approval_log = ClientApprovalLog.objects.create(
                        client=client,
                        admin=admin,
                        admin_approval_status=admin_approval_status
                    )
                    serializer = ClientApprovalLogSerializer(new_approval_log)
                    client.admin_approval_status = admin_approval_status
                    client.save()
                    try:
                        send_mail(
                            'Notification Email',
                            f'Your account is {admin_approval_status}.',
                            'orddel@viltco.com',
                            [f"{client.email}"],
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


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        return data


# ------------------------------------------------------------------------------------------------------------------------


class ClientLogin(TokenObtainPairView):

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
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"message": "Password is required!"})
        try:
            serializer_class = MyTokenObtainPairSerializer(data=request.data)
            if serializer_class.is_valid(self):
                user = User.objects.get(username=username)
                client = Client.objects.get(username=username)
                is_active = user.is_active
                otp_status = client.otp_status
                approval_status = client.admin_approval_status
                if is_active and otp_status and approval_status == 'approved':

                    return Response(status=status.HTTP_200_OK, data={"client_id": client.id,
                                                                     "data": serializer_class.validated_data})
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED,
                                    data={"data": "Client user not authorized"})

            else:
                print("invalid username and password")

        except:
            try:
                user = User.objects.get(username=username)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'User or Password is not correct'})
            is_active = user.is_active
            if not is_active:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "The account is not verified via email"})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "Username or Password is not correct"})


# ------------------------------------------------------------------------------------------------------------------------


class PendingApprovalListApiView(APIView):

    def get(self, request):
        try:
            admin_approval_status = self.request.query_params.get('admin_approval_status').lower()
            try:
                client = Client.objects.filter(admin_approval_status=admin_approval_status)
                serializer = ClientSerializer(client, many=True)
                print(admin_approval_status, client)
                if not client:
                    return Response(status=status.HTTP_200_OK,
                                    data={"message": "Client table is empty"})
                return Response(status=status.HTTP_200_OK,
                                data={"pending_approval_list": serializer.data})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            pass


