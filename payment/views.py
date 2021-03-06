from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date
from .models import *
from .serializers import *
from order.serializers import OrderDetailSerializer
# Create your views here.


class GetInvNumberAPIView(APIView):

    def get(self, request, id=None):
        if id:
            try:
                invoice = Invoice.objects.filter(order=id).last()
                orderdetail = OrderDetail.objects.get(id=id)
                order_id = orderdetail.id
                if invoice:
                    inv_number_list = invoice.inv_number.split("_")
                    inv_number = int(inv_number_list[3])
                    inv_number += 1
                    invoice_order_no = f"Inv#{str(order_id).zfill(5)}_{date.today().strftime('%Y')}_{str(inv_number).zfill(5)}"
                else:
                    inv_number = 1
                    invoice_order_no = f"Inv#{str(order_id).zfill(5)}_{date.today().strftime('%Y')}_{str(inv_number).zfill(5)}"

            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "order not found"})

            return Response(status=status.HTTP_200_OK, data={"invoice_number": invoice_order_no})

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "id not provided"})


class ListCreateInvoice(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def create(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid(self):
            data = serializer.validated_data
            try:
                print(data["order"])
                invoice = Invoice.objects.get(order=data["order"])
                print(invoice)
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Invoice already exists"})

            except:
                serializer.save()
                return Response(status=status.HTTP_201_CREATED, data={"response": serializer.data})


class RetrieveUpdateDestroyInvoice(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class GetDeliveryNoteNumberAPIView(APIView):

    def get(self, request, id=None):
        if id:
            try:
                order_detail = OrderDetail.objects.get(order_box=id)
                delivery_person_id = order_detail.delivery_person.id
                prefix = order_detail.delivery_person.first_name[0:3].upper()
                delivery_note = DeliveryNote.objects.filter(order=order_detail).last()

                if delivery_note:
                    do_number_list = delivery_note.do_number.split("_")
                    do_number = int(do_number_list[3])
                    do_number += 1
                    delivery_note_no = f"DN#{prefix}_{str(delivery_person_id).zfill(5)}_{date.today().strftime('%Y')}_{str(do_number).zfill(5)}"

                else:
                    do_number = 1
                    delivery_note_no = f"DN#{prefix}_{str(delivery_person_id).zfill(5)}_{date.today().strftime('%Y')}_{str(do_number).zfill(5)}"

            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "order_box not found"})

            return Response(status=status.HTTP_200_OK, data={"dn_number": delivery_note_no})

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "id not provided"})


class CreateDeliveryNote(APIView):
    def post(self, request):
        try:
            order_id = request.data['order_id']
            delivery_note_number = request.data['delivery_note_number']
            delivery_note = request.data['delivery_note']
            purchased_products = request.data['purchased_products']

            try:
                order_detail = OrderDetail.objects.get(id=order_id)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': f'Order with {order_id} does not exist'})
            # list_of_orderprods = order_detail.order_products.all()
            order_prod_list = order_detail.order_products.all()
            for order_prod in order_prod_list:
                order_prod.purchased_quantity = order_prod.quantity
            for product in purchased_products:
                try:
                    order_prod_obj = order_detail.order_products.get(product=product['product_id'])
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": f"product with {product['product_id']}"
                                                                                            f"does not exist in order"})
                print(order_prod_obj.purchased_quantity)
                order_prod_obj.purchased_quantity = product['purchased_qty']
                order_prod_obj.save()

            try:
                DeliveryNote.objects.get(order=order_detail)
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Delivery note already exists"})
            except:
                DeliveryNote.objects.create(order=order_detail, do_number=delivery_note_number, delivery_note=delivery_note)
            return Response(status=status.HTTP_200_OK, data={'message': 'Delivery note created'})

        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'message': 'Something went wrong!'})


class GenerateInvoiceAPIView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                order_detail = OrderDetail.objects.get(order_box=id)
                serializer = OrderDetailSerializer(order_detail)
                response = serializer.data
                order_prods = []
                order_prods.extend(order_detail.order_products.all())
                for order_prod in order_prods:
                    order_prod.purchased_quantity = order_prod.quantity
                    order_prod.save()
                products_details = []
                total_purchased_qty = 0
                total_vat = 0
                total_amount = 0
                for prod in order_prods:
                    product = {}
                    order_prod_obj = OrderProduct.objects.get(id=prod.id)
                    product['product_id'] = order_prod_obj.product.id
                    product['product_name'] = order_prod_obj.product.name
                    product['product_unit'] = order_prod_obj.product.unit
                    product['avg_price'] = order_prod_obj.product.avg_price
                    product['ordered_quantity'] = order_prod_obj.quantity
                    product['purchased_qty'] = order_prod_obj.purchased_quantity
                    if product['purchased_qty'] != 0:
                        total_purchased_qty += product['purchased_qty']
                        product['unit_sales_price'] = order_prod_obj.unit_sale_price
                        product['vat_amount'] = order_prod_obj.product.vat * order_prod_obj.unit_sale_price
                        total_vat += product['vat_amount']
                    # product['total_amount'] = order_prod_obj.total_amount
                        product['amount'] = product['vat_amount'] + product['unit_sales_price']
                        total_amount += product['amount']
                        product['supplier_market'] = order_prod_obj.supplier
                    products_details.append(product)
                response['order_products'] = products_details
                order_b_obj = OrderBox.objects.get(id=response['order_box'])
                if order_b_obj.client != None:
                    response['client'] = order_b_obj.client.first_name + " " + order_b_obj.client.last_name
                delivery_note_obj = DeliveryNote.objects.get(order=order_detail.id)
                response['delivery_note'] = delivery_note_obj.delivery_note
                response['total_qty'] = total_purchased_qty
                response['total_vat'] = total_vat
                response['total_amount'] = total_amount
                delivery_person_obj = DeliveryPerson.objects.get(id=response['delivery_person'])
                response['delivery_person_name'] = delivery_person_obj.first_name + " " + delivery_person_obj.last_name
                response['delivery_person_address'] = delivery_person_obj.address
                # shipment_address = ClientShipmentAddress.objects.get(id=response['shipment_address'])
                # response['shipment_address_detail'] = shipment_address.shipment_address
                if response['status'] == 'in_progress':
                    response['status'] = 'in progress'
                return Response(status=status.HTTP_200_OK, data={"order": response})

            except:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"message": "Something went wrong"})

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Order Box ID not entered"})