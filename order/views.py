from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt import authentication
from rest_framework.response import Response
from .models import *
from datetime import date
from django.db.models import Sum
from .serializers import *
from django.db import connection
import json
import random
import string


# Create your views here.
class CreateOrderBoxApiView(APIView):
    def post(self, request):
        client_id = request.data['client_id']

        try:
            client = Client.objects.get(id=client_id)
            try:
                # try:
                #     order_box = OrderBox.objects.get(client=client.id)
                #     print(order_box)
                #     serializer = OrderBoxSerializer(order_box)
                #     return Response(status=status.HTTP_400_BAD_REQUEST, data={"cart_already_present": serializer.data["client"]})
                #
                # except:

                cart = OrderBox.objects.create(
                    client=client
                )
                instance = OrderBox.objects.get(id=cart.id)
                serializer = OrderBoxSerializer(instance)
                return Response(status=status.HTTP_201_CREATED, data={"cart": serializer.data})

            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "error in record creation"})

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "Invalid data entered"})


class ListOrderBoxApiView(APIView):
    def get(self, request, id=None):
        try:
            if id:
                order_box = OrderBox.objects.get(id=id)
                data_to_pass = OrderBoxSerializer(order_box)
            else:
                order_box = OrderBox.objects.all().order_by('-date_created')
                data_to_pass = OrderBoxSerializer(order_box, many=True)
            return Response(status=status.HTTP_200_OK, data={"order_box": data_to_pass.data})
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "No Order-box(es) Found"})


class UpdateOrderBoxApiView(APIView):
    def put(self, request):
        try:
            order_box_id = request.data['order_box']
            client_id = request.data['client_id']


            try:
                order_box = OrderBox.objects.get(id=order_box_id)

                try:
                    client = Client.objects.get(id=client_id)

                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "client not found"})

            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "cart not entered or not found"})

            OrderBox.objects.filter(id=order_box_id).update(
                    client=client
                )
            order_box = OrderBox.objects.get(id=order_box_id)
            print("Cart ID :", order_box)
            data_to_pass = OrderBoxSerializer(order_box)
            return Response(status=status.HTTP_200_OK, data={"updated_order_box": data_to_pass.data})

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Exception": e})


class DeleteOrderBoxApiView(APIView):
    def delete(self, request, id=None):
        if id:
            try:
                order_box = OrderBox.objects.get(id=id)
                data = OrderBoxSerializer(order_box)
                order_box.delete()
                return Response(status=status.HTTP_200_OK, data={"message": f"Deleted orderbox of client {data.data['client']}"})
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"Exception": e})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error_msg": "ID missing from URL"})


class AddOrderBoxProductsApiView(APIView):

    def post(self, request):

    # try:
        order_box_id = request.data['order_box']
        products = request.data['order_products']
        try:
            order_box = OrderBox.objects.get(id=order_box_id)
            for prod in products:
                product = Product.objects.get(id=prod['id'])
                # price = product.avg_price
                try:
                    order_pro = OrderProduct.objects.get(order_box=order_box, product=product)
                    order_pro.quantity += prod['quantity']
                    order_pro.total_amount += prod['total_amount']
                    order_pro.save()

                except:
                    OrderProduct.objects.create(
                        order_box=order_box,
                        product=product,
                        quantity=prod['quantity'],
                        total_amount=prod['total_amount']
                    )
            add_to_order = OrderProduct.objects.filter(order_box=order_box)
            data_list = []
            grand_total = 0
            for obj in add_to_order:
                serializer = OrderProductsSerializer(obj)
                data_list.append(serializer.data)
                grand_total += obj.total_amount

            # order_box.save()
            order_box = {
                    "order_box": order_box.id,
                    "grand_total": grand_total,
                    "client": str(order_box.client.first_name + " " + order_box.client.last_name),
                    "order_products": data_list
            }

            return Response(status=status.HTTP_201_CREATED, data={"order_box": order_box})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": e})
    # except Exception as e:
    #     return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": e})


class ListOrderBoxProductsApiView(APIView):

    def get(self, request, id=None):

        try:
            if id:
                order_products = OrderProduct.objects.filter(order_box__id=id)
                data_list = []
                grand_total = 0
                order_box = {}
                for obj in order_products:
                    serializer = OrderProductsSerializer(obj)
                    data_list.append(serializer.data)
                    grand_total += obj.total_amount

                if len(data_list) != 0:
                    order_box_id = int(str(data_list[0]['order_box']))
                    order_box_obj = OrderBox.objects.get(id=order_box_id)
                    order_box["order_box_id"] = order_box_obj.id
                    order_box["grand_total"] = grand_total
                    order_box["client"] = str(order_box_obj.client.user)
                    order_box["products"] = data_list
                    return Response(status=status.HTTP_200_OK, data={"order_box_products": order_box})
                else:
                    return Response(status=status.HTTP_204_NO_CONTENT, data={"message": "No order box products"})

            else:
                order_box_obj = OrderBox.objects.all().order_by('-date_created')

                order_box = []
                for o_obj in order_box_obj:
                    order_box_dict = {}
                    order_box_dict["order_box_id"] = o_obj.id
                    order_box_prod = o_obj.orderproducts_set.all()
                    serializer = OrderProductsSerializer(order_box_prod, many=True)
                    order_box_dict["products"] = serializer.data
                    order_box.append(order_box_dict)

                return Response(status=status.HTTP_200_OK, data={"carts": order_box})


        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "No Order-box(es) Found"})


class UpdateOrderBoxProductsApiView(generics.UpdateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductsSerializer


class DeleteOrderBoxProductsApiView(APIView):

    def delete(self, request, id=None):
        if id:
            try:
                order_box_products = OrderProduct.objects.filter(order_box__id=id)
                print(order_box_products)
                serializer = OrderProductsSerializer(order_box_products, many=True)
                order_box_products.delete()
                return Response(status=status.HTTP_200_OK, data={"status": "Successfully Deleted"})

            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"Exception": e})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error_msg": "ID missing from URL"})


class CreateOrderApiView(APIView):

    # def generate_ordernum(self):
    #     letters_and_digits = string.ascii_letters + string.digits
    #     rand_alphanum = ''.join((random.choice(letters_and_digits) for i in range(16)))
    #     return rand_alphanum

    def post(self, request):

        # while True:
        #     try:
        #         purchase_ordernum = self.generate_ordernum()
        #         order = OrderDetail.objects.get(purchase_order_no=purchase_ordernum)
        #         if not order:
        #             break
        #
        #     except:
        #         break



        order_box = request.data['order_box']
        purchase_order_no = request.data['purchase_order_no']
        order_title = request.data['order_title']
        delivery_person = request.data['delivery_person']
        order_delivery_datetime = request.data['order_delivery_datetime']
        # shipment_address = request.data['shipment_address']
        business = request.data['business_id']
        delivery_notes = request.data['delivery_notes']
        comment = request.data['comment']
        distance = request.data['distance']
        # total_units_ordered = request.data['total_units_ordered']
        delivery_status = request.data['status'].lower()
        payment_type = request.data['payment_type'].lower()
        try:
            order_box_obj = OrderBox.objects.get(id=order_box)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "cart does not exist"})

        try:
            delivery_obj = DeliveryPerson.objects.get(id=delivery_person)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "delivery person does not exist"})

        try:
            business_obj = ClientBusinessDetail.objects.get(id=business)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "business does not exist"})
        #
        # try:
        #
        #     order = OrderDetail.objects.get(order_box=order_box_obj)
        #     print(order)
        #     return Response(status=status.HTTP_409_CONFLICT, data={"error": "record already exists"})
        #
        # except:
        # try:
        client_id = order_box_obj.client.id
        # print(client_id)
        client = Client.objects.get(id=client_id)
        # orderdetail = OrderDetail.objects.filter(order_box=order_box).last()
        # if orderdetail:
        #     po_number_list = orderdetail.purchase_order_no.split("_")
        #     po_number = int(po_number_list[2])
        #     po_number += 1
        #     purchase_order_no = f"PO#{str(client.id).zfill(5)}_{date.today().strftime('%m%d%y')}_{str(po_number).zfill(5)}"
        # else:
        #     po_number = 1
        #     purchase_order_no = f"PO#{str(client.id).zfill(5)}_{date.today().strftime('%m%d%y')}_{str(po_number).zfill(5)}"

        list_of_order_prods = []
        list_of_order_prods.extend(order_box_obj.orderproduct_set.all())
        # print(list_of_order_prods)
        order = OrderDetail.objects.create(
            order_box=order_box_obj,
            business=business_obj,
            purchase_order_no=purchase_order_no,
            order_title=order_title,
            delivery_person=delivery_obj,
            order_delivery_datetime=order_delivery_datetime,
            # shipment_address=shipment_obj,
            delivery_notes=delivery_notes,
            comment=comment,
            distance=distance,
            # total_units_ordered=total_units_ordered,
            status=delivery_status,
            payment_type=payment_type
        )
        for prod in list_of_order_prods:
            order.order_products.add(prod.id)
        # print(client.number_of_order)
        if client.no_of_invoices != 0:
            client.no_of_invoices -= 1
        client.number_of_order += 1
        client.save()
        serializer = OrderDetailSerializer(order)
        response = serializer.data
        products_details = []
        for prod in list_of_order_prods:
            product = {}
            order_prod_obj = OrderProduct.objects.get(id=prod.id)
            product['product_name'] = order_prod_obj.product.name
            product['product_unit'] = order_prod_obj.product.unit
            product['quantity'] = order_prod_obj.quantity
            product['total_amount'] = order_prod_obj.total_amount
            products_details.append(product)
        response['order_products'] = products_details
        return Response(status=status.HTTP_201_CREATED, data={"order": response})

        # except:
        #     return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "record_creation_failed"})


class UpdateOrderApiView(generics.UpdateAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


class ListOrderApiView(APIView):
    def get(self, request, id=None):
        # try:
        if id:
            order_detail = OrderDetail.objects.get(order_box=id)
            data_to_pass = OrderDetailSerializer(order_detail)
        else:
            order_detail = OrderDetail.objects.all().order_by('-order_created_datetime')
            data_to_pass = OrderDetailSerializer(order_detail, many=True)

        response = data_to_pass.data
        if not isinstance(response, list):
            order_box = response['order_box']
            # order_box_obj = OrderBox.objects.get(id=order_box)
            order_detail = OrderDetail.objects.get(order_box=order_box)
            order_prods = []
            order_prods.extend(order_detail.order_products.all())
            products_details = []
            for prod in order_prods:
                product = {}
                order_prod_obj = OrderProduct.objects.get(id=prod.id)
                product['product_id'] = order_prod_obj.product.id
                product['product_name'] = order_prod_obj.product.name
                product['product_unit'] = order_prod_obj.product.unit
                product['avg_price'] = order_prod_obj.product.avg_price
                product['quantity'] = order_prod_obj.quantity
                product['total_amount'] = order_prod_obj.total_amount
                products_details.append(product)
            response['order_products'] = products_details
            order_b_obj = OrderBox.objects.get(id=response['order_box'])
            if order_b_obj.client != None:
                response['client'] = order_b_obj.client.first_name + " " + order_b_obj.client.last_name
            delivery_person_obj = DeliveryPerson.objects.get(id=response['delivery_person'])
            response['delivery_person_name'] = delivery_person_obj.first_name + " " + delivery_person_obj.last_name
            # shipment_address = ClientShipmentAddress.objects.get(id=response['shipment_address'])
            # response['shipment_address_detail'] = shipment_address.shipment_address
            if response['status'] == 'in_progress':
                response['status'] = 'in progress'
            return Response(status=status.HTTP_200_OK, data={"order": response})

        else:
            response_list = []
            for res in response:
                order_detail_obj = OrderDetail.objects.get(order_box=res['order_box'])
                res['no_of_products'] = order_detail_obj.order_products.count()
                order_b_obj = OrderBox.objects.get(id=res['order_box'])
                order_prods = []
                order_prods.extend(order_b_obj.orderproduct_set.all())
                products_details = []
                for prod in order_prods:
                    product = {}
                    order_prod_obj = OrderProduct.objects.get(id=prod.id)
                    product['product_name'] = order_prod_obj.product.name
                    product['product_unit'] = order_prod_obj.product.unit
                    product['quantity'] = order_prod_obj.quantity
                    product['total_amount'] = order_prod_obj.total_amount
                    products_details.append(product)
                res['order_products'] = products_details
                if order_b_obj.client != None:
                    res['client'] = order_b_obj.client.first_name + " " + order_b_obj.client.last_name
                delivery_person_obj = DeliveryPerson.objects.get(id=res['delivery_person'])
                res['delivery_person_name'] = delivery_person_obj.first_name + " " + delivery_person_obj.last_name
                # shipment_address = ClientShipmentAddress.objects.get(id=res['shipment_address'])
                # res['shipment_address_detail'] = shipment_address.shipment_address
                response_list.append(res)
            return Response(status=status.HTTP_200_OK, data={"orders": response_list})

        # except Exception as e:
        #     return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "error in retrieving orders"})


class DeleteOrderApiView(generics.DestroyAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


class GetPONumberAPIView(APIView):

    def get(self, request, id=None):
        if id:
            try:
                order_box = OrderBox.objects.get(id=id)
                client = order_box.client.id
                prefix = order_box.client.first_name[0:3].upper()
                orderdetail = OrderDetail.objects.filter(order_box__client=client).last()
                print(orderdetail)

                # order_detail_client = orderdetail.order_box.client
                
                if orderdetail:
                    po_number_list = orderdetail.purchase_order_no.split("_")
                    po_number = int(po_number_list[3])
                    po_number += 1
                    purchase_order_no = f"PO#{prefix}_{str(client).zfill(5)}_{date.today().strftime('%Y')}_{str(po_number).zfill(5)}"
                else:
                    po_number = 1
                    purchase_order_no = f"PO#{prefix}_{str(client).zfill(5)}_{date.today().strftime('%Y')}_{str(po_number).zfill(5)}"

            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "order_box not found"})

            return Response(status=status.HTTP_200_OK, data={"po_number": purchase_order_no})

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "id not provided"})


class ListOrdersAssignedAPIView(APIView):
    def get(self, request):
        delivery_person = self.request.query_params.get('delivery_person_id')
        choice = self.request.query_params.get('choice').lower()
        try:
            if choice == 'all':
                order_detail = OrderDetail.objects.filter(delivery_person=delivery_person)
                serializer = OrderDetailSerializer(order_detail, many=True)

            elif choice == 'pending':
                order_detail = OrderDetail.objects.filter(delivery_person=delivery_person, status=choice)
                serializer = OrderDetailSerializer(order_detail, many=True)

            elif choice == 'purchased' : 
                order_detail = OrderDetail.objects.filter(delivery_person=delivery_person, status=choice)
                serializer = OrderDetailSerializer(order_detail, many=True)

            elif choice == 'in_progress':
                order_detail = OrderDetail.objects.filter(delivery_person=delivery_person, status=choice)
                serializer = OrderDetailSerializer(order_detail, many=True)

            elif choice == 'delivered':
                order_detail = OrderDetail.objects.filter(delivery_person=delivery_person, status=choice)
                serializer = OrderDetailSerializer(order_detail, many=True)

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Invalid Option entered'})

            data_list = []
            for data in serializer.data:
                order_detail = OrderDetail.objects.get(id=data['id'])
                data['no_of_items'] = order_detail.order_products.count()
                if order_detail.order_box.client != None:
                    data['client_name'] = order_detail.order_box.client.first_name + " " + order_detail.order_box.client.last_name
                # print(order_detail.order_box.client.first_name)
                shipment_address = ClientShipmentAddress.objects.get(id=order_detail.shipment_address.id)
                data['shipment_address'] = shipment_address.shipment_address
                delivery_person = DeliveryPerson.objects.get(id=order_detail.delivery_person.id)
                data['delivery_person_name'] = delivery_person.first_name + " " + delivery_person.last_name
                data_list.append(data)
            return Response(status=status.HTTP_200_OK, data={'response': data_list})

        except:
            pass


class ConsolidatePurchaseAPIView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                sql = f"""SELECT M.status,M.delivery_person_id,d.product_id,sum(d.quantity) as qty, s.id as pid, s.name, s.unit, s.avg_price 
                        FROM order_orderdetail M inner join order_orderproduct D on D.order_box_id=M.order_box_id 
                        INNER JOIN products_product S ON S.ID=D.PRODUCT_ID 
                        where M.status='in_progress' and delivery_person_id={id}
                        group by M.status,M.delivery_person_id,d.product_id,s.id, s.name,s.unit 
                        order by s.name
                        """
                cursor = connection.cursor()
                cursor.execute(sql)
                #
                rows = cursor.fetchall()
                consolidated_purchases = []
                for row in rows:
                    data_dict = {'status': row[0], 'delivery_person_id': row[1], 'product_id': row[2], 'qty': row[3],
                                 'product_name': row[5], 'unit': row[6], 'avg_price': row[7]}
                    consolidated_purchases.append(data_dict)

                if consolidated_purchases:
                    return Response(status=status.HTTP_200_OK, data={'data': consolidated_purchases,
                                                                     'status_code': 200,
                                                                     'message': "Successful"
                                                                     })
                else:
                    return Response(status=status.HTTP_200_OK, data={'data': 'No orders found against the given ID',
                                                                     'status_code': 200,
                                                                     'message': "Successful"
                                                                     })
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={
                                                                        'status_code': 400,
                                                                        'message': "Unsuccessful"
                                                                        })

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={
                                                             'status_code': 400,
                                                             'message': "Unsuccessful"
                                                             })


class ListClientOrdersAPIView(APIView):
    def get(self, request):
        client = self.request.query_params.get('client_id')
        choice = self.request.query_params.get('choice').lower()
        try:
            if choice == 'all':
                order_detail = OrderDetail.objects.filter(order_box__client=client)
                serializer = OrderDetailSerializer(order_detail, many=True)

            elif choice == 'pending':
                order_detail = OrderDetail.objects.filter(order_box__client=client, status=choice)
                serializer = OrderDetailSerializer(order_detail, many=True)

            elif choice == 'in_progress':
                order_detail = OrderDetail.objects.filter(order_box__client=client, status=choice)
                serializer = OrderDetailSerializer(order_detail, many=True)

            elif choice == 'delivered':
                order_detail = OrderDetail.objects.filter(order_box__client=client, status=choice)
                serializer = OrderDetailSerializer(order_detail, many=True)

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Invalid Option entered'})

            data_list = []
            for data in serializer.data:
                order_detail = OrderDetail.objects.get(id=data['id'])
                data['no_of_items'] = order_detail.order_products.count()
                if order_detail.order_box.client is not None:
                    data['client_name'] = order_detail.order_box.client.first_name + " " + order_detail.order_box.client.last_name
                # print(order_detail.order_box.client.first_name)
                shipment_address = ClientShipmentAddress.objects.get(id=order_detail.shipment_address.id)
                data['shipment_address'] = shipment_address.shipment_address
                delivery_person = DeliveryPerson.objects.get(id=order_detail.delivery_person.id)
                data['delivery_person_name'] = delivery_person.first_name + " " + delivery_person.last_name
                data_list.append(data)
            return Response(status=status.HTTP_200_OK, data={'response': data_list})

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'failed to retrieve records'})


class InsertPurchaseDetailsAPIView(APIView):
    def put(self, request):
        # try:
        for detail in request.data['purchase_details']:
            delivery_person = detail['delivery_person_id']
            product_id = detail['product_id']
            supplier = detail['supplier']
            unit_purchase_price = detail['unit_purchase_price']
            profit_margin = detail['profit_margin']
            profit_margin_choice = detail['profit_margin_choice']
            unit_sales_price = detail['unit_sales_price']

            sql = f"""UPDATE 
                        ORDER_ORDERPRODUCT D
                     SET 
                        profit_margin={profit_margin},
                        supplier='{supplier}', 
                        unit_purchase_price={unit_purchase_price}, 
                        unit_sale_price={unit_sales_price},
                        profit_margin_choice='{profit_margin_choice}'
                    FROM 
                        ORDER_ORDERDETAIL M 
                    WHERE 
                        M.order_box_id=D.order_box_id AND D.product_id={product_id} AND M.delivery_person_id={delivery_person} ;
                 """
            cursor = connection.cursor()
            cursor.execute(sql)
            order_details = OrderDetail.objects.filter(delivery_person=delivery_person, status='in_progress')
            order_details.update(status = 'purchased')
            # for order in order_details:
            #     order.status = 'purchased'

        return Response(status=status.HTTP_200_OK, data={'response': "Purchase Details submitted successfully",
                                                         'status_code': '200',
                                                         'message': 'Successful'
                                                         })

        # except:
        #     return Response(status=status.HTTP_400_BAD_REQUEST, data={'response': 'Unable to submit purchase details',
        #                                                               'status_code': '200',
        #                                                               'message': 'Unsuccessful'
        #                                                               })
