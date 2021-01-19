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
                try:
                    cart = Cart.objects.get(client=client.id)
                    print(cart)
                    serializer = CartSerializer(cart)
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={"cart_already_present": serializer.data["client"]})

                except:
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


class CartProductsApiView(APIView):

    def post(self, request):

        try:
            cart_id = request.data['cart_id']
            products = request.data['cart_products']
            try:
                cart = Cart.objects.get(id=cart_id)
                for prod in products:
                    product = Product.objects.get(id=prod['id'])
                    price = product.avg_price
                    add_to_cart = CartProducts.objects.create(
                        cart=cart,
                        product=product,
                        quantity=prod['quantity'],
                        total_amount=price*prod['quantity']
                    )
                add_to_cart = CartProducts.objects.filter(cart=cart)
                data_list = []
                for obj in add_to_cart:
                    serializer = CartProductsSerializer(obj)
                    data_list.append(serializer.data)
                    cart.grand_total += obj.total_amount

                cart.save()
                cart = {
                        "cart_id": cart.id,
                        "grand_total": cart.grand_total,
                        "client": str(cart.client.user),
                        "cart_products": data_list
                }

                return Response(status=status.HTTP_201_CREATED, data={"cart": cart})
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": e})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": e})
