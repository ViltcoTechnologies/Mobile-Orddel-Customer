from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django_email_verification import sendConfirm


# Category Registration API
class CreateCategoryApiView(APIView):

    def get(self, request, id=None):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        category_name = request.data['name']
        try:
            saved_data = Category.objects.get(name=category_name)
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=f"Category name with '{category_name}' already exists!")
        except:
            try:
                new_product_details = Category.objects.create(
                    name=request.data['name'],
                    description=request.data['description']
                )
                new_product_details.save()
                serializer = CategorySerializer(new_product_details)
                return Response(status=status.HTTP_200_OK,
                                data={"category_created": serializer.data})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data="There was a error creating record!")


# Category List API
class ListCategoryApiView(APIView):

    def get(self, request, id=None):
        if id:
            try:
                category = Category.objects.get(id=id)
                serializer = CategorySerializer(category)
                return Response(status=status.HTTP_200_OK, data={"category": serializer.data})
            except:
                return Response(status=status.HTTP_200_OK, data="Database is empty!")
        else:
            try:
                category = Category.objects.all()
                serializer = CategorySerializer(category, many=True)
                return Response(status=status.HTTP_200_OK, data={"categories": serializer.data})
            except:
                return Response(status=status.HTTP_404_NOT_FOUND, data="Database is empty!")


# Category Update API
class UpdateCategoryApiView(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def put(self, request, id=None):
        category_name = request.data['name']
        try:
            saved_data = Category.objects.filter(name=category_name)
            saved_data.update(
                description=request.data['description']
            )
            serializer = CategorySerializer(saved_data, many=True)
            return Response(status=status.HTTP_200_OK,
                            data={'updated_category': serializer.data})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data="No Record Found!")


# Category Delete API
class DeleteCategoryApiView(APIView):

    def get(self, request, id=None):
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        if id:
            # try:
            saved_data = DeliveryPerson.objects.get(id=id)
            User.objects.get(id=saved_data.user.id).delete()
            return Response(status=status.HTTP_200_OK, data={'Record deleted against email': saved_data.username})
            # except:
            #     return Response(status=status.HTTP_404_NOT_FOUND, data="No Record Found!")
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Error Msg": "ID missing from URL"})


# ------------------------------------------------------------------------------------------------------------------------


# Product Registration API
class CreateProductApiView(APIView):

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


# Product List API
class ListProductApiView(APIView):

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


# Product List based on Category ID
class ListCategoryProductApiView(APIView):

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


# Product Update API
class UpdateProductApiView(APIView):

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


# Product Delete API
class DeleteProductApiView(APIView):

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


# Review Registration API
class CreateReviewApiView(APIView):

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


# Review List API
class ListReviewApiView(APIView):

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


# Review List based on Product ID
class ListProductReviewApiView(APIView):

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


# Review Update API
class UpdateReviewApiView(APIView):

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


# Review Delete API
class DeleteReviewApiView(APIView):

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
