from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt import authentication
from django_email_verification import sendConfirm
from rest_framework.response import Response
from .models import *
from .serializers import *
import json
# CRUD operations of client

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

    def put(self, request):
        try:
            saved_data = User.objects.get(email = request.data['email'])
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
            return Response(status=status.HTTP_200_OK, data={"updated_details": serializer.data})
        except AssertionError as err:
            return Response(status=status.HTTP_404_NOT_FOUND, data=err)


class DeleteClientApiView(APIView):

    def delete(self,  request, id = None):
        if id:
            # try:
            client = Client.objects.get(id = id)
            user = User.objects.get(id = client.user.id)
            # print(client.user__id)
            username = user.username
            user.delete()
            return Response(status=status.HTTP_200_OK, data={"Deleted record against username": username})
            # except Exception as e:
            #     return Response(status = status.HTTP_400_BAD_REQUEST, data={"Exception" : e})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Error Msg" : "ID missing from URL"})


class ListClientsApiView(APIView):

    def get(self, request, id = None):
        try:
            if id:
                clients = Client.objects.get(id = id)
                data_to_pass = ClientSerializer(clients)
            else:
                clients = Client.objects.all().order_by('-date_created')
                data_to_pass = ClientSerializer(clients, many=True)
            return Response(status=status.HTTP_200_OK, data={"all_clients": data_to_pass.data})
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"No Clients Found"})



# CRUD operations of Business Detail
class BusinessDetailInsertApiView(APIView):

    def post(self, request):
        try:
            username = request.data['username']
            business_name = request.data['business_name']
            business_nature = request.data['business_nature']
            business_type = request.data['business_type']
            business_logo = request.data['business_logo']

            client = Client.objects.get(username = username)
            business_detail = BusinessDetail.objects.create(
                client = client,
                name = business_name,
                nature = business_nature,
                type = business_type,
                logo = business_logo
            )
            print(business_detail.id)
            bd = BusinessDetail.objects.filter(id=business_detail.id, client = client)
            data_to_pass = BusinessDetailSerializer(bd, many=True)
            return Response(status = status.HTTP_200_OK, data={"business_details" : data_to_pass.data[0]})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Exception": e})


class ListBusinessDetailsApiView(APIView):

    def get(self, request, id= None):
        if id:
            try:
                business_detail = BusinessDetail.objects.get(id = id)
                data_to_pass = BusinessDetailSerializer(business_detail)

            except Exception as e:
                return Response(status = status.HTTP_400_BAD_REQUEST, data={'Error' : e})

        else:
            try:
                business_detail = BusinessDetail.objects.all()
                data_to_pass = BusinessDetailSerializer(business_detail, many=True)
            except Exception as e:
                return Response(status = status.HTTP_400_BAD_REQUEST, data={'Error' : e})

        return Response(status=status.HTTP_200_OK, data={"business_details": data_to_pass.data})



class ListClientBusinessDetailsApiView(APIView):

    def get(self, request, id = None):
        if id:
            try:
                business_detail = BusinessDetail.objects.get(client__id = id)
                data_to_pass = BusinessDetailSerializer(business_detail)
                return Response(status=status.HTTP_200_OK, data={"client_businesses": data_to_pass.data})

            except Exception as e:
                return Response(status = status.HTTP_404_NOT_FOUND, data={'Error' : 'client not found'})



class UpdateBusinessApiView(APIView):

    def put(self, request, id = None):
        try:
            business_id = request.data['id']
            business_name = request.data['business_name']
            business_nature = request.data['business_nature']
            business_type = request.data['business_type']
            business_logo = request.data['business_logo']

            business_detail = BusinessDetail.objects.filter(id = business_id).update(
                name=business_name,
                nature=business_nature,
                type=business_type,
                logo=business_logo
            )
            print("Business Detail id :", business_detail)
            bd = BusinessDetail.objects.get(id=business_id)
            data_to_pass = BusinessDetailSerializer(bd)
            return Response(status=status.HTTP_200_OK, data={"updated_business_details": data_to_pass.data})

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Exception": e})

class DeleteBusinessApiView(APIView):

    def delete(self, request, id = None):
        if id:
            try:
                business = BusinessDetail.objects.get(id = id).delete()
                name = business.name
                return Response(status = status.HTTP_200_OK, data = {"business_delete": name})
            except Exception as e:
                return Response(status = status.HTTP_404_NOT_FOUND, data={"error": "record not found against the given id"})


# CRUD of Shipment Address

class ShipmentAddressCreateApiView(APIView):

    def post(self, request, id = None):
        client_id = request.data['client_id']
        shipment_address = request.data['shipment_address']

        client = Client.objects.get(id = client_id)
        shipment_record = ShipmentAddress.objects.create(
            client = client,
            shipment_address = shipment_address
        )
        # shipment = ShipmentAddress.objects.get(id = shipment_record.id)
        data_to_pass = ShipmentAddressSerializer(shipment_record)
        return Response(status = status.HTTP_200_OK, data={"shipment_address_created": data_to_pass.data})


class ListShipmentAddressApiView(APIView):

    def get(self, request, id=None):
        if id:
            try:
                shipment_address = ShipmentAddress.objects.get(id=id)
                data_to_pass = ShipmentAddressSerializer(shipment_address)

            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'Error': e})

        else:
            try:
                shipment_address = ShipmentAddress.objects.all()
                data_to_pass = ShipmentAddressSerializer(shipment_address, many=True)
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'Error': e})

        return Response(status=status.HTTP_200_OK, data={"shipment_addresses": data_to_pass.data})

class ListClientShipmentAddressApiView(APIView):

    def get(self, request, id = None):
        if id:
            try:
                shipment = ShipmentAddress.objects.filter(client__id = id)
                data_to_pass = ShipmentAddressSerializer(shipment, many=True)
                return Response(status=status.HTTP_200_OK, data={"client_shipment_addresses": data_to_pass.data})

            except Exception as e:
                return Response(status = status.HTTP_404_NOT_FOUND, data={'Error' : 'client not found'})


class UpdateShipmentAddressApiView(APIView):

    def put(self, request):
        try:
            shipment_id = request.data['shipment_id']
            shipment_address = request.data['shipment_address']

            shipment_rec = ShipmentAddress.objects.filter(id = shipment_id)
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

    def delete(self, request, id = None):
        if id:
            try:
                shipment_rec = ShipmentAddress.objects.get(id = id)
                address = shipment_rec.shipment_address
                shipment_rec.delete()
                return Response(status = status.HTTP_200_OK, data={"record_deleted":address})

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
            bank_record = BankDetails.objects.create(
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
            return Response(status = status.HTTP_400_BAD_REQUEST, data={"Exception" : e})


class BankDetailsUpdateApiView(APIView):
    def put(self, request, id=None):
        try:
            bank_detail_id = request.data['id']
            bank_name = request.data['bank_name']
            branch_code = request.data['branch_code']
            credit_card_no = request.data['credit_card_no']
            sort_code = request.data['sort_code']
            credit_card_expiry = request.data['credit_card_expiry']

            bank_detail = BankDetails.objects.filter(id=bank_detail_id).update(
                bank_name=bank_name,
                branch_code=branch_code,
                credit_card_no=credit_card_no,
                sort_code=sort_code,
                credit_card_expiry=credit_card_expiry
            )
            print("Bank Detail id :", bank_detail)
            bd = BankDetails.objects.get(id=bank_detail_id)
            data_to_pass = BankDetailsSerializer(bd)
            return Response(status=status.HTTP_200_OK, data={"updated_business_details": data_to_pass.data})

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Exception": e})

class ListBankDetailsApiView(APIView):
    def get(self, request, id=None):
            if id:
                try:
                    bank_detail = BankDetails.objects.get(id=id)
                    data_to_pass = BankDetailsSerializer(bank_detail)

                except Exception as e:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'Error': e})

            else:
                try:
                    bank_details = BankDetails.objects.all()
                    data_to_pass = BankDetailsSerializer(bank_details, many=True)
                except Exception as e:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'Error': e})

            return Response(status=status.HTTP_200_OK, data={"bank_details": data_to_pass.data})

class ListClientBankDetailsApiView(APIView):

    def get(self, request, id=None):
        if id:
            try:
                bank_details = BankDetails.objects.filter(client__id=id)
                data_to_pass = BankDetailsSerializer(bank_details, many=True)
                return Response(status=status.HTTP_200_OK, data={"bank_details": data_to_pass.data})

            except Exception as e:
                return Response(status=status.HTTP_404_NOT_FOUND, data={'Error': 'client not found'})


class DeleteBankDetailsApiView(APIView):

    def delete(self, request, id = None):
        if id:
            try:
                bank_rec = BankDetails.objects.get(id = id)
                bank_name = bank_rec.bank_name
                bank_rec.delete()
                return Response(status = status.HTTP_200_OK, data={"record_deleted":bank_name})

            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"Error": "Unable to delete record"})


class PackageCreateApiView(APIView):
    def post(self, request):
        try:
            name = request.data['name']
            package = Package.objects.get(name = name)
            return Response(status = status.HTTP_400_BAD_REQUEST, data = {"error" : f"{name} record already exists"})

        except:
            try:

                description = request.data['description']
                price = request.data['price']


                package_record = Package.objects.create(
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
            package = Package.objects.get(name = name)
            return Response(status = status.HTTP_400_BAD_REQUEST, data = {"error" : f"{package.name} record already exists"})
        except:
            try:
                package_id = request.data['id']
                name = request.data['name']
                description = request.data['description']
                price = request.data['price']


                package_detail = Package.objects.filter(id=package_id).update(
                    name=name,
                    description=description,
                    price=price,

                )
                print("Package ID :", package_detail)
                bd = Package.objects.get(id=package_id)
                data_to_pass = PackageSerializer(bd)
                return Response(status=status.HTTP_200_OK, data={"updated_business_details": data_to_pass.data})

            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"Exception": e})


class ListPackagesApiView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                package = Package.objects.filter(id=id)
                data_to_pass = PackageSerializer(package, many=True)
                return Response(status=status.HTTP_200_OK, data={"package_details": data_to_pass.data})

            except Exception as e:
                return Response(status=status.HTTP_404_NOT_FOUND, data={'Error': 'package not found'})
        else:
            try:
                package = Package.objects.all()
                data_to_pass = PackageSerializer(package, many=True)
                return Response(status=status.HTTP_200_OK, data={"all_package": data_to_pass.data})

            except Exception as e:
                return Response(status=status.HTTP_404_NOT_FOUND, data={'Error': 'package not found'})

class ListClientPackagesApiView(APIView):
    def get(self, request, id=None):
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
                package_rec = Package.objects.get(id=id)
                package_name = package_rec.name
                package_rec.delete()
                return Response(status=status.HTTP_200_OK, data={"record_deleted": package_name})

            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"Error": "Unable to delete record"})

