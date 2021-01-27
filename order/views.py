from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt import authentication
from rest_framework.response import Response
from .models import *
from .serializers import *
import json
import random
import string

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


class ListCartApiView(APIView):
    def get(self, request, id=None):
        try:
            if id:
                cart = Cart.objects.get(id=id)
                data_to_pass = CartSerializer(cart)
            else:
                cart = Cart.objects.all().order_by('-date_created')
                data_to_pass = CartSerializer(cart, many=True)
            return Response(status=status.HTTP_200_OK, data={"cart(s)": data_to_pass.data})
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"No Carts Found"})


class UpdateCartApiView(APIView):
    def put(self, request):
        try:
            cart_id = request.data['cart_id']
            client_id = request.data['client_id']


            try:
                cart = Cart.objects.get(id=cart_id)

                try:
                    client = Client.objects.get(id=client_id)

                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "client not found"})

            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "cart not entered or not found"})

            Cart.objects.filter(id=cart_id).update(
                    client=client
                )
            cart = Cart.objects.get(id=cart_id)
            print("Cart ID :", cart)
            data_to_pass = CartSerializer(cart)
            return Response(status=status.HTTP_200_OK, data={"updated_business_details": data_to_pass.data})

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Exception": e})


class DeleteCartApiView(APIView):
    def delete(self, request, id=None):
        if id:
            try:
                cart = Cart.objects.get(id=id)
                data = CartSerializer(cart)
                cart.delete()
                return Response(status=status.HTTP_200_OK, data={"Deleted cart of client ": data.data['client']})
            except Exception as e:
                return Response(status = status.HTTP_400_BAD_REQUEST, data={"Exception": e})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Error Msg": "ID missing from URL"})


class AddCartProductsApiView(APIView):

    def post(self, request):

        try:
            cart_id = request.data['cart_id']
            products = request.data['cart_products']
            try:
                cart = Cart.objects.get(id=cart_id)
                for prod in products:
                    product = Product.objects.get(id=prod['id'])
                    price = product.avg_price
                    try:
                        cart_prod = CartProducts.objects.get(cart=cart, product=product)
                        cart_prod.quantity += prod['quantity']
                        cart_prod.total_amount += price*prod['quantity']
                        cart_prod.save()

                    except:
                        CartProducts.objects.create(
                            cart=cart,
                            product=product,
                            quantity=prod['quantity'],
                            total_amount=price*prod['quantity']
                        )
                add_to_cart = CartProducts.objects.filter(cart=cart)
                data_list = []
                grand_total = 0
                for obj in add_to_cart:
                    serializer = CartProductsSerializer(obj)
                    data_list.append(serializer.data)
                    grand_total += obj.total_amount

                cart.save()
                cart = {
                        "cart_id": cart.id,
                        "grand_total": grand_total,
                        "client": str(cart.client.user),
                        "cart_products": data_list
                }

                return Response(status=status.HTTP_201_CREATED, data={"cart": cart})
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": e})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": e})


class ListCartProductsApiView(APIView):

    def get(self, request, id=None):

        try:
            if id:
                cart_products = CartProducts.objects.filter(cart__id=id)
                data_list = []
                grand_total = 0
                cart = {}
                for obj in cart_products:
                    serializer = CartProductsSerializer(obj)
                    data_list.append(serializer.data)
                    grand_total += obj.total_amount

                cart_id = int(str(data_list[0]['cart']))
                cart_obj = Cart.objects.get(id=cart_id)
                cart["cart_id"] = cart_obj.id
                cart["grand_total"] = grand_total
                cart["client"] = str(cart_obj.client.user)
                cart["products"] = data_list
                return Response(status=status.HTTP_200_OK, data={"cart_products": cart})

            else:
                cart_obj = Cart.objects.all().order_by('-date_created')

                carts = []
                for c_obj in cart_obj:
                    cart_dict = {}
                    cart_dict["cart_id"] = c_obj.id
                    cart_prod = c_obj.cartproducts_set.all()
                    serializer = CartProductsSerializer(cart_prod, many=True)
                    cart_dict["products"] = serializer.data
                    carts.append(cart_dict)

                return Response(status=status.HTTP_200_OK, data={"carts": carts})


        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"No Carts Found"})


class UpdateCartProductsApiView(APIView):
    pass
#     def put(self, request):
#         cart_id = request.data["cart_id"]
#         grand_total = request.data["grand_total"]
#         client = request.data["client"]
#         products = request.data["products"]
#
#         for prod in products:
#             total_amount = prod['product']
#             cartprod = CartProducts.objects.filter(id=prod['id']).update(
#                 product=prod['product'],
#                 quantity=prod['quantity']
#
#
#             )


class DeleteCartProductsApiView(APIView):

    def delete(self, request, id=None):
        if id:
            try:
                cart_products = CartProducts.objects.filter(cart__id=id)
                print(cart_products)
                serializer = CartProductsSerializer(cart_products, many=True)
                cart_products.delete()
                return Response(status=status.HTTP_200_OK, data={"deleted_products": serializer.data})

            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"Exception": e})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error_msg": "ID missing from URL"})


class CreateOrderApiView(APIView):

    def generate_ordernum(self):
        letters_and_digits = string.ascii_letters + string.digits
        rand_alphanum = ''.join((random.choice(letters_and_digits) for i in range(16)))
        return rand_alphanum

    def post(self, request):

        while True:
            try:
                purchase_ordernum = self.generate_ordernum()
                order = OrderDetail.objects.get(purchase_order_no=purchase_ordernum)
                if not order:
                    break

            except:
                break

        cart = request.data['cart']
        purchase_order_no = purchase_ordernum
        order_title = request.data['order_title']
        delivery_person = request.data['delivery_person']
        order_delivery_datetime = request.data['order_delivery_datetime']
        shipment_address = request.data['shipment_address']
        delivery_notes = request.data['delivery_notes']
        comment = request.data['comment']
        distance = request.data['distance']
        total_units_ordered = request.data['total_units_ordered']
        delivery_status = request.data['status']
        payment_type = request.data['payment_type']
        try:
            cart_obj = Cart.objects.get(id=cart)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "cart does not exist"})

        try:
            delivery_obj = DeliveryPerson.objects.get(id=delivery_person)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "delivery person does not exist"})

        try:
            shipment_obj = ShipmentAddress.objects.get(id=shipment_address)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "shipment address does not exist"})

        try:
            print("here")
            order = OrderDetail.objects.get(cart=cart_obj)
            print(order)
            return Response(status=status.HTTP_409_CONFLICT, data={"error": "record already exists"})

        except:
            try:
                order = OrderDetail.objects.create(
                    cart=cart_obj,
                    purchase_order_no=purchase_order_no,
                    order_title=order_title,
                    delivery_person=delivery_obj,
                    order_delivery_datetime=order_delivery_datetime,
                    shipment_address=shipment_obj,
                    delivery_notes=delivery_notes,
                    comment=comment,
                    distance=distance,
                    total_units_ordered=total_units_ordered,
                    status=delivery_status,
                    payment_type=payment_type
                )

                serializer = OrderDetailSerializer(order)
                return Response(status=status.HTTP_201_CREATED, data={"order": serializer.data})

            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "record_creation_failed"})


class UpdateOrderApiView(APIView):
    pass