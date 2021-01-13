from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt import authentication
from rest_framework.response import Response
from .models import *
from .serializers import *
import json


# Create your views here.

class CreateCartApiView(APIView):
    def post(self, request):
        client_id = request.data['client_id']
        grand_total = request.data['grand_total']

        try:
            client = Client.objects.get(id=client_id)
            try:
                cart = Cart.objects.create(
                    client=client,
                    grand_total=grand_total
                )
                instance = Cart.objects.get(id=cart.id)
                serializer = CartSerializer(instance)
                return Response(status=status.HTTP_201_CREATED, data={"cart": serializer.data})

            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "error in record creation"})

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "Invalid data entered"})


class AddToCartApiView(APIView):
    def post(self, request, id = None):
        cart_id = request.data['cart_id']
        products = request.data['cart_products']
        print(cart_id)
        print(products)
        return Response(status=status.HTTP_201_CREATED)
        # quantity = request.data['quantity']
        # number_of_boxes = request.data['number_of_boxes']
        # quantity = request.data['quantity']
        # total_amount = request.data['total_amount']

        # try:
        #     client = Client.objects.get(id=client_id)
        #     product = Client.objects.get(id=product_id)
        #     try:
        #         cart = AddToCart.objects.create(
        #             client=client,
        #             product=product,
        #             weight=weight,
        #             number_of_boxes=number_of_boxes,
        #             quantity=quantity,
        #             total_amount=total_amount
        #         )
        #         instance = AddToCart.objects.get(id = cart.id)
        #         serializer = AddToCartSerializer(instance)
        #         return Response(status=status.HTTP_201_CREATED, data={"cart": serializer.data})
        #     except:
        #         return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "error in created record"})
        #
        # except:
        #     return Response(status = status.HTTP_400_BAD_REQUEST, data={"error":"Invalid data entered"})
