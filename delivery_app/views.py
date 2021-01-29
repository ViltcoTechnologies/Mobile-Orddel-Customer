from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework_simplejwt import authentication
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django_email_verification import sendConfirm
from ordel.verificaton import TwilioVerification


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
                                current_location=current_location,
                                buying_capacity=buying_capacity,
                                phone_number=phone_number,
                                address=address,
                                gender=gender,
                                image=image
                            )
                            new_delivery_person.save()
                            serializer = DeliveryPersonSerializer(new_delivery_person)
                            new_auth_user.save()
                            twilio_verification = TwilioVerification(str(phone_number))
                            twilio_verification.send_otp()

                            print("Data Saved: ", new_delivery_person)
                            return Response(status=status.HTTP_200_OK,
                                            data={"delivery_person_created": serializer.data})
                        except:
                            return Response(status=status.HTTP_400_BAD_REQUEST,
                                            data="Error! delivery_person was not created "
                                                 "but auth_user was created "
                                                 "deleting auth-user entry")
                    except:
                        return Response(status=status.HTTP_400_BAD_REQUEST,
                                        data="Email already registered")
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data="Error! Make sure you're not missing one of the "
                                     "following required fields: (first_name, last_name, "
                                     "email, phone_number, password)")
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
class UpdateDeliveryPersonApiView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = (authentication.JWTAuthentication,)

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def put(self, request, id=None):
        try:
            # optional parameters
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            phone_number = request.data['phone_number']
            address = request.data['address']
            current_location = request.data['current_location']
            no_of_orders = request.data['no_of_orders']
            buying_capacity = request.data['buying_capacity']
            total_amount_shopped = request.data['total_amount_shopped']
            gender = request.data['gender']
            image = request.data['image']
            approval_status = request.data['approval_status']
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
                            address=address,
                            current_location=current_location,
                            no_of_orders=no_of_orders,
                            buying_capacity=buying_capacity,
                            total_amount_shopped=total_amount_shopped,
                            gender=gender,
                            image=image,
                            approval_status=approval_status
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
                                 "leave fields blank, then send null or empty"
                                 "and for approval_status send either 'True' or 'False'")


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

            delivery_person = DeliveryPerson.objects.get(username=username)
            business_detail = DeliveryPersonBusinessDetail.objects.create(
                delivery_person=delivery_person,
                name=business_name,
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


class ListClientBusinessDetailsApiView(APIView):

    def get(self, request, id = None):
        if id:
            try:
                business_detail = DeliveryPersonBusinessDetail.objects.get(delivery_person__id=id)
                data_to_pass = DeliveryPersonBusinessDetailSerializer(business_detail)
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

            business_detail = DeliveryPersonBusinessDetail.objects.filter(id=business_id).update(
                name=business_name,
                nature=business_nature,
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


class BankDetailsCreateApiView(APIView):

    def post(self, request):
        try:
            delivery_person_id = request.data['delivery_person']
            bank_name = request.data['bank_name']
            branch_code = request.data['branch_code']
            credit_card_no = request.data['credit_card_no']
            sort_code = request.data['sort_code']
            credit_card_expiry = request.data['credit_card_expiry']

            delivery_person = DeliveryPerson.objects.get(id=delivery_person_id)
            bank_record = DeliveryPersonBankDetail.objects.create(
                delivery_person=delivery_person,
                bank_name=bank_name,
                branch_code=branch_code,
                credit_card_no=credit_card_no,
                sort_code=sort_code,
                credit_card_expiry=credit_card_expiry
            )
            data_to_pass = DeliveryPersonBankDetailSerializer(bank_record)
            return Response(status=status.HTTP_200_OK,
                            data={"bank_details_created": data_to_pass.data})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"Exception" : e})


class BankDetailsUpdateApiView(APIView):

    def put(self, request):
        try:
            bank_detail_id = request.data['id']
            bank_name = request.data['bank_name']
            branch_code = request.data['branch_code']
            credit_card_no = request.data['credit_card_no']
            sort_code = request.data['sort_code']
            credit_card_expiry = request.data['credit_card_expiry']

            bank_detail = DeliveryPersonBankDetail.objects.filter(id=bank_detail_id).update(
                bank_name=bank_name,
                branch_code=branch_code,
                credit_card_no=credit_card_no,
                sort_code=sort_code,
                credit_card_expiry=credit_card_expiry
            )
            print("Bank Detail id :", bank_detail)
            bd = DeliveryPersonBankDetail.objects.get(id=bank_detail_id)
            data_to_pass = BankDetailsSerializer(bd)
            return Response(status=status.HTTP_200_OK,
                            data={"updated_business_details": data_to_pass.data})

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"Exception": e})


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


class ListClientBankDetailsApiView(APIView):

    def get(self, request):
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


class ListPackagesApiView(APIView):

    def get(self, request):
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
                package = DeliveryPersonPackage.objects.all()
                data_to_pass = DeliveryPersonPackageSerializer(package, many=True)
                return Response(status=status.HTTP_200_OK,
                                data={"all_package": data_to_pass.data})

            except Exception as e:
                return Response(status=status.HTTP_404_NOT_FOUND,
                                data={'Error': 'package not found'})


class ListClientPackagesApiView(APIView):

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


class UpdateDeliveryPersonApprovalStatus(APIView):

    def post(self, request):
        try:
            delivery_person_id = request.data['delivery_person']
            delivery_person = DeliveryPerson.objects.get(id=delivery_person_id)
            approval_status = request.data['approval_status']
            approval_status.lower()
            if approval_status == 'approved':
                delivery_person.admin_approval_status = 'approved'
                delivery_person.save()

            elif approval_status == 'unapproved':
                delivery_person.admin_approval_status = 'unapproved'
                delivery_person.save()

            elif approval_status == 'pending':
                delivery_person.admin_approval_status = 'pending'
                delivery_person.save()

            elif approval_status == 'cancelled':
                delivery_person.admin_approval_status = 'cancelled'
                delivery_person.save()

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"error": "incorrect option for approval status"})
            send_mail(
                'Notification Email',
                f'Your account has been {approval_status}.',
                'orddel@viltco.com',
                [f"{client.email}"],
                fail_silently=False,
            )
            return Response(status=status.HTTP_200_OK, data={"approval_status": client.admin_approval_status})

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "client id incorrect"})
