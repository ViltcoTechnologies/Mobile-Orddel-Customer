from django.shortcuts import render
from django.conf import settings
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from datetime import date
from django.db.models import Avg, Q, F, Sum, FloatField
from .models import *
from .serializers import *
from order.serializers import OrderDetailSerializer, OrderProductsSerializer
from django.views.generic import View as view
from .utils import *
import stripe
import datetime
import json
from pprint import pprint
stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.


class GetInvNumberAPIView(APIView):

    def get(self, request, id=None):
        if id:
            try:
                orderdetail = OrderDetail.objects.get(id=id)
                order_id = orderdetail.id
                prefix = orderdetail.delivery_person.first_name.upper()
                delivery_person_id = orderdetail.delivery_person.id
                invoice = Invoice.objects.filter(order__delivery_person=delivery_person_id).last()
                if invoice:
                    inv_number_list = invoice.inv_number.split("_")
                    inv_number = int(inv_number_list[3])
                    inv_number += 1
                    invoice_order_no = f"Inv#{prefix[:3]}_{str(order_id).zfill(5)}_{date.today().strftime('%Y')}_{str(inv_number).zfill(5)}"
                else:
                    inv_number = 1
                    invoice_order_no = f"Inv#{prefix[:3]}_{str(order_id).zfill(5)}_{date.today().strftime('%Y')}_{str(inv_number).zfill(5)}"

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
                delivery_note = DeliveryNote.objects.filter(order__delivery_person=delivery_person_id).last()

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
                order_prod.save()
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
                delivery_note_obj = DeliveryNote.objects.get(order=order_detail)
                delivery_note_obj.order = order_detail
                delivery_note_obj.do_number = delivery_note_number
                delivery_note_obj.delivery_note = delivery_note
                delivery_note_obj.save()
            except Exception as e:
                print(e.args)
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
                    # product['avg_price'] = order_prod_obj.product.avg_price
                    product['ordered_quantity'] = order_prod_obj.quantity
                    product['purchased_qty'] = order_prod_obj.purchased_quantity
                    if product['purchased_qty'] != 0:
                        total_purchased_qty += product['purchased_qty']
                        product['unit_sales_price'] = float("{:.2f}".format(order_prod_obj.unit_sale_price))
                        product['vat_amount'] = float("{:.2f}".format(order_prod_obj.product.vat * order_prod_obj.unit_sale_price))
                        total_vat += product['vat_amount']
                    # product['total_amount'] = order_prod_obj.total_amount
                        product['amount'] = float("{:.2f}".format((product['vat_amount'] + product['unit_sales_price']) * product['purchased_qty']))
                        total_amount += product['amount']
                        # product['supplier_market'] = order_prod_obj.supplier
                    else:
                        product['unit_sales_price'] = 0
                        product['vat_amount'] = 0
                        product['amount'] = 0
                        product['supplier_market'] = ""
                    products_details.append(product)
                response['order_products'] = products_details
                order_b_obj = OrderBox.objects.get(id=response['order_box'])
                if order_b_obj.client != None:
                    response['client'] = order_b_obj.client.first_name + " " + order_b_obj.client.last_name
                delivery_note_obj = DeliveryNote.objects.get(order=order_detail.id)
                response['delivery_note'] = delivery_note_obj.delivery_note
                response['total_qty'] = float("{:.2f}".format(total_purchased_qty))
                response['total_vat'] = float("{:.2f}".format(total_vat))
                response['total_amount'] = float("{:.2f}".format(total_amount))
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


class ViewInvoiceApiView(APIView):
    def get(self, request, id=None):
        if id:
            # try:
            try:
                invoice = Invoice.objects.get(order=id)
            except Exception as e:
                print(e)
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Invoice does not exist'})
            serializer = InvoiceSerializer(invoice)
            response = serializer.data
            order_prods = []
            order_prods.extend(invoice.order.order_products.all())
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
                # product['avg_price'] = order_prod_obj.product.avg_price
                product['ordered_quantity'] = order_prod_obj.quantity
                product['purchased_qty'] = order_prod_obj.purchased_quantity
                if product['purchased_qty'] != 0:
                    total_purchased_qty += product['purchased_qty']
                    product['unit_sales_price'] = float("{:.2f}".format(order_prod_obj.unit_sale_price))
                    product['vat_amount'] = float("{:.2f}".format(order_prod_obj.product.vat * order_prod_obj.unit_sale_price))
                    total_vat += product['vat_amount']
                    # product['total_amount'] = order_prod_obj.total_amount
                    product['amount'] = float("{:.2f}".format((product['vat_amount'] + product['unit_sales_price']) * product['purchased_qty']))
                    total_amount += product['amount']
                    # product['supplier_market'] = order_prod_obj.supplier

                else:
                    product['unit_sales_price'] = 0
                    product['vat_amount'] = 0
                    product['amount'] = 0
                    product['supplier_market'] = ""
                products_details.append(product)

            response['order_products'] = products_details
            order_b_obj = OrderBox.objects.get(id=invoice.order.order_box.id)
            if order_b_obj.client != None:
                response['client'] = order_b_obj.client.first_name + " " + order_b_obj.client.last_name
                response['client_id'] = order_b_obj.client.id
            delivery_note_obj = DeliveryNote.objects.get(order=invoice.order)
            response['delivery_note'] = delivery_note_obj.delivery_note
            response['total_qty'] = float("{:.2f}".format(total_purchased_qty))
            response['total_vat'] = float("{:.2f}".format(total_vat))
            response['total_amount'] = float("{:.2f}".format(total_amount))
            delivery_person_obj = DeliveryPerson.objects.get(id=invoice.order.delivery_person.id)
            response['delivery_person_id'] = delivery_person_obj.id
            response['delivery_person_name'] = delivery_person_obj.first_name + " " + delivery_person_obj.last_name
            response['delivery_person_address'] = delivery_person_obj.address
            try:
                response['business_address'] = invoice.order.business.address
            except Exception as e:
                print(e)
                response['business_address'] = ""
            response['purchase_order_no'] = invoice.order.purchase_order_no
            response['order_delivery_datetime'] = invoice.order.order_delivery_datetime.strftime('%d-%m-%Y %H:%M')
            # shipment_address = ClientShipmentAddress.objects.get(id=response['shipment_address'])
            # response['shipment_address_detail'] = shipment_address.shipment_address
            return Response(status=status.HTTP_200_OK, data={"order": response})

            # except:
            #     return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"message": "Something went wrong"})

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Order ID not entered"})


def prepare_invoice(invoice_id):
    if invoice_id:
        try:
            invoice = Invoice.objects.get(order=invoice_id)
        except:
            raise Exception
        serializer = InvoiceSerializer(invoice)
        response = serializer.data
        order_prods = []
        order_prods.extend(invoice.order.order_products.all())
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
            # product['avg_price'] = order_prod_obj.product.avg_price
            product['ordered_quantity'] = order_prod_obj.quantity
            product['purchased_qty'] = order_prod_obj.purchased_quantity
            if product['purchased_qty'] != 0:
                total_purchased_qty += product['purchased_qty']
                product['unit_sales_price'] = float("{:.2f}".format(order_prod_obj.unit_sale_price))
                product['vat_amount'] = float("{:.2f}".format(order_prod_obj.product.vat * order_prod_obj.unit_sale_price))
                total_vat += product['vat_amount']
                # product['total_amount'] = order_prod_obj.total_amount
                product['amount'] = float("{:.2f}".format((product['vat_amount'] + product['unit_sales_price']) * product['purchased_qty']))
                total_amount += product['amount']
                # product['supplier_market'] = order_prod_obj.supplier
            else:
                product['unit_sales_price'] = 0
                product['vat_amount'] = 0
                product['amount'] = 0
                product['supplier_market'] = ""
            products_details.append(product)
        response['order_products'] = products_details
        order_b_obj = OrderBox.objects.get(id=invoice.order.order_box.id)
        if order_b_obj.client != None:
            response['client'] = order_b_obj.client.first_name + " " + order_b_obj.client.last_name
        delivery_note_obj = DeliveryNote.objects.get(order=invoice.order)
        response['delivery_note'] = delivery_note_obj.delivery_note
        response['total_qty'] = total_purchased_qty
        response['total_vat'] = float("{:.2f}".format(total_vat))
        response['total_amount'] = float("{:.2f}".format(total_amount))
        response['net_total_without_vat'] = response['total_amount'] - response['total_vat']
        delivery_person_obj = DeliveryPerson.objects.get(id=invoice.order.delivery_person.id)
        dp_bank_details = DeliveryPersonBankDetail.objects.filter(delivery_person=delivery_person_obj).last()
        if dp_bank_details:
            response['bank_name'] = dp_bank_details.bank_name
            response['account_title'] = dp_bank_details.account_title
            response['credit_card_no'] = dp_bank_details.credit_card_no
            response['sort_code'] = dp_bank_details.sort_code
        dp_business_detail = DeliveryPersonBusinessDetail.objects.filter(delivery_person=delivery_person_obj).last()
        if dp_business_detail:
            response['dp_business_name'] = dp_business_detail.name
            response['dp_business_address'] = dp_business_detail.address
        response['delivery_person_name'] = delivery_person_obj.first_name + " " + delivery_person_obj.last_name
        response['delivery_person_address'] = delivery_person_obj.address
        response['business_address'] = invoice.order.business.address
        response['purchase_order_no'] = invoice.order.purchase_order_no[3:]
        response['inv_number'] = response['inv_number'][4:]
        response['order_delivery_datetime'] = invoice.order.order_delivery_datetime.strftime('%d-%m-%Y %H:%M')
        # shipment_address = ClientShipmentAddress.objects.get(id=response['shipment_address'])
        # response['shipment_address_detail'] = shipment_address.shipment_address

        return response


class GeneratePDFInvoiceAPIView(APIView):

    def get(self, request, id=None):
        if id:
            response = prepare_invoice(invoice_id=id)
            order_detail = OrderDetail.objects.get(id=response['order'])
            try:
                response["client_logo"] = order_detail.order_box.client.image.url
            except Exception as e:
                print(e.args)
                response['client_logo'] = ""
            try:
                response["delivery_person_logo"] = order_detail.delivery_person.image.url
            except Exception as e:
                print(e.args)
                response["delivery_person_logo"] = ""
            try:
                delivery_person_name = response['delivery_person_name']
                print(delivery_person_name)
            except:
                delivery_person_name = ""
            template = get_template("invoice_template.html")
            context = {
                "response": response
            }
            html = template.render(context)
            pdf = render_to_pdf("invoice_template.html", context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "Invoice_%s.pdf" % delivery_person_name
                content = "inline; filename='%s'" %(filename)
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename='%s'" %(filename)
                response['Content-Disposition'] = content
                return response

            return HttpResponse("Not found")


class CreatePaymentMethod(APIView):
    serializer_class = CreatePaymentMethodSerializer

    def post(self, request):
        serializer_class = CreatePaymentMethodSerializer(data=request.data)
        if serializer_class.is_valid():
            card_number = serializer_class.validated_data['card_number']
            cvc = serializer_class.validated_data['cvc']
            expiry_date = serializer_class.validated_data['expiry_date']
            print(expiry_date.month)

            response = stripe.PaymentMethod.create(
                type="card",
                card={
                    "number": card_number,
                    "exp_month": expiry_date.month,
                    "exp_year": expiry_date.year,
                    "cvc": cvc,
                    },
                )

            return Response(status=status.HTTP_200_OK, data=response)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer_class.errors)


class SaveStripeInfo(APIView):
    serializer_class = SaveStripInfoSerializer

    def post(self, request):
        serializer_class = SaveStripInfoSerializer(data=request.data)

        if serializer_class.is_valid():
            card_number = serializer_class.validated_data['card_number']
            cvc = serializer_class.validated_data['cvc']
            expiry_date = serializer_class.validated_data['expiry_date']
            id = serializer_class.validated_data['id']
            user_type = serializer_class.validated_data['user_type']
            extra_msg = 'Payment details saved and customer created'
            email = ''
            client = None
            delivery_person = None
            if user_type == 'client':
                try:
                    client = Client.objects.get(id=id)
                    email = client.username
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={
                                                                        'message': 'Client does not exist'
                                                                                })
            elif user_type == 'delivery_person':
                try:
                    delivery_person = DeliveryPerson.objects.get(id=id)
                    email = delivery_person.username
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={
                                                                            'message': 'Delivery Person does not exist'
                                                                              })

            customer_data = stripe.Customer.list(email=email).data

            if len(customer_data) == 0:
                try:
                    response = stripe.PaymentMethod.create(
                        type="card",
                        card={
                            "number": card_number,
                            "exp_month": expiry_date.month,
                            "exp_year": expiry_date.year,
                            "cvc": cvc,
                        },
                    )
                except stripe.error.CardError as e:
                    return Response(status=e.http_status, data={
                                                                'code': e.code,
                                                                'param': e.param,
                                                                'message': e.user_message
                                                                })
                payment_method_id = response['id']
                customer = stripe.Customer.create(
                    email=email, payment_method=payment_method_id)
            else:
                customer = customer_data[0]
                response = stripe.PaymentMethod.list(
                    customer=customer,
                    type="card",
                )
                payment_method_id = response['data'][0]['id']
                print(payment_method_id)
                print(customer)
                extra_msg = "Customer and payment details already existed."

            if client:
                obj, created = ClientPaymentDetails.objects.get_or_create(
                    client=client,
                    customer_id=customer['id'],
                    payment_method_id=payment_method_id
                )
            elif delivery_person:
                obj, created = DeliveryPaymentDetails.objects.get_or_create(
                    delivery_person=delivery_person,
                    customer_id=customer['id'],
                    payment_method_id=payment_method_id
                )

            return Response(status=status.HTTP_200_OK,
                            data={
                                    'message': 'Success',
                                    'data': {
                                        'customer_id': customer.id,
                                        'extra_msg': extra_msg
                                        }
                                  })

        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': serializer_class.errors})


class PaymentAPIView(APIView):
    serializer_class = MakePaymentSerializer

    def post(self, request):
        serializer_class = MakePaymentSerializer(data=request.data)

        if serializer_class.is_valid():
            user_id = serializer_class.validated_data['user_id']
            user_type = serializer_class.validated_data['user_type']
            package_id = serializer_class.validated_data['package_id']

            if user_type == 'client':
                try:
                    obj = Client.objects.get(id=user_id)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Client does'
                                                                                         'not exist'})
                try:
                    package_obj = ClientPackage.objects.get(id=package_id)
                    amount = package_obj.price

                except:
                    return Response(status=status.HTTP_200_OK, data={'message': 'Package does not exist'})
                try:
                    client_payment_details = ClientPaymentDetails.objects.get(client=user_id)
                    customer = client_payment_details.customer_id
                    payment_method_id = client_payment_details.payment_method_id
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Client Payment'
                                                                                         'details does '
                                                                                         'not exist'})
            elif user_type == 'delivery_person':
                try:
                    obj = DeliveryPerson.objects.get(id=user_id)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Delivery Person '
                                                                                         'does not exist'})
                try:
                    package_obj = DeliveryPersonPackage.objects.get(id=package_id)
                    amount = package_obj.price

                except:
                    return Response(status=status.HTTP_200_OK, data={'message': 'Package does not exist'})

                try:
                    delivery_person_payment_details = DeliveryPaymentDetails.objects.get(delivery_person=user_id)
                    customer = delivery_person_payment_details.customer_id
                    payment_method_id = delivery_person_payment_details.payment_method_id
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Delivery Person Payment'
                                                                                         'details does '
                                                                                         'not exist'})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Invalid choice'})

            response = stripe.PaymentIntent.create(
                customer=customer,
                payment_method=payment_method_id,
                currency='EUR',
                amount=int(float(amount)*100),
                confirm=True)
            if response['status'] == 'succeeded':
                obj.package = package_obj
                if package_obj.id != 3:
                    if obj.no_of_invoices == -1:
                        obj.no_of_invoices += 1
                        obj.no_of_invoices += package_obj.no_of_invoices
                    else:
                        obj.no_of_invoices += package_obj.no_of_invoices
                else:
                    obj.no_of_invoices = -1
                obj.save()
                if user_type == 'client':
                    ClientPackageLog.objects.create(
                        client=obj,
                        package=package_obj,
                        date_expiry=datetime.datetime.now() + datetime.timedelta(package_obj.validity_in_days),
                        status='active'

                    )
                elif user_type == 'delivery_person':
                    DeliveryPersonPackageLog.objects.create(
                        delivery_person=obj,
                        package=package_obj,
                        date_expiry=datetime.datetime.now() + datetime.timedelta(package_obj.validity_in_days),
                        status='active'

                    )
            return Response(status=status.HTTP_200_OK, data={"message": "Payment Succeeded "
                                                                        "and invoices added",
                                                             "total_invoices": obj.no_of_invoices
                                                            })

        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer_class.errors)


class ShowCardAPIView(APIView):
    def get(self, request, id=None):
        if id:
            user_type = self.request.query_params.get('user_type')
            if user_type == 'client':
                try:
                    client_payment_details = ClientPaymentDetails.objects.get(client=id)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Client Payment details does not exist'})
                response = stripe.PaymentMethod.list(
                    customer=client_payment_details.customer_id,
                    type="card",
                )
                card_brand = response['data'][0]['card']['brand']
                last4 = response['data'][0]['card']['last4']

                return Response(status=status.HTTP_200_OK, data={
                                                                'message': 'Success',
                                                                'card': {
                                                                        'card_brand': card_brand,
                                                                        'last4': last4
                                                                        }
                                                                })

            elif user_type == 'delivery_person':
                try:
                    delivery_payment_details = DeliveryPaymentDetails.objects.get(delivery_person=id)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Delivery Person Payment '
                                                                                         'details does not exist'})

                response = stripe.PaymentMethod.list(
                    customer=delivery_payment_details.customer_id,
                    type="card",
                )
                card_brand = response['data'][0]['card']['brand']
                last4 = response['data'][0]['card']['last4']

                return Response(status=status.HTTP_200_OK, data={
                                                                'message': 'Success',
                                                                'card': {
                                                                        'card_brand': card_brand,
                                                                        'last4': last4
                                                                        }
                                                                })
            else:
                return Response(status=status.HTTP_200_OK, data={'error': 'Invalid Choice !'})


def prepare_delivery_note(order_id):
    if order_id:
        try:
            delivery_note = DeliveryNote.objects.get(order=order_id)
        except:
            raise Exception
        serializer = DeliveryNoteSerializer(delivery_note)
        response = serializer.data
        order_prods = []
        order_prods.extend(delivery_note.order.order_products.all())
        products_details = []
        total_purchased_qty = 0
        total_vat = 0
        total_amount = 0
        for prod in order_prods:
            product = {}
            order_prod_obj = OrderProduct.objects.get(id=prod.id)
            product['product_name'] = order_prod_obj.product.name
            product['product_unit'] = order_prod_obj.product.unit
            product['purchased_qty'] = order_prod_obj.purchased_quantity
            if product['purchased_qty'] != 0:
                total_purchased_qty += product['purchased_qty']
            products_details.append(product)
        response['order_products'] = products_details
        order_b_obj = OrderBox.objects.get(id=delivery_note.order.order_box.id)
        if order_b_obj.client != None:
            response['client'] = order_b_obj.client.first_name + " " + order_b_obj.client.last_name
        response['delivery_note'] = delivery_note.delivery_note
        response['total_qty'] = total_purchased_qty
        delivery_person_obj = DeliveryPerson.objects.get(id=delivery_note.order.delivery_person.id)
        response['delivery_person_name'] = delivery_person_obj.first_name + " " + delivery_person_obj.last_name
        response['delivery_person_address'] = delivery_person_obj.address
        response['business_address'] = delivery_note.order.business.address
        response['purchase_order_no'] = delivery_note.order.purchase_order_no[3:]
        response['do_number'] = response['do_number'][3:]
        response['order_delivery_datetime'] = delivery_note.order.order_delivery_datetime.strftime('%d-%m-%Y %H:%M')
        dp_business_detail = DeliveryPersonBusinessDetail.objects.filter(delivery_person=delivery_person_obj).last()
        if dp_business_detail:
            response['dp_business_name'] = dp_business_detail.name
            response['dp_business_address'] = dp_business_detail.address
        # shipment_address = ClientShipmentAddress.objects.get(id=response['shipment_address'])
        # response['shipment_address_detail'] = shipment_address.shipment_address

        return response


class GenerateDeliveryNotePDF(APIView):
    def get(self, request, id=None):
        if id:
            response = prepare_delivery_note(order_id=id)
            order_detail = OrderDetail.objects.get(id=response['order'])
            try:
                response["client_logo"] = order_detail.order_box.client.image.url
            except:
                response['client_logo'] = ""
            try:
                response["delivery_person_logo"] = order_detail.delivery_person.image.url
            except:
                response["delivery_person_logo"] = ""
            try:
                delivery_person_name = response['delivery_person_name']
                print(delivery_person_name)
            except:
                delivery_person_name = ""
            template = get_template("delivery_note.html")
            context = {
                "response": response
            }
            html = template.render(context)
            pdf = render_to_pdf("delivery_note.html", context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "Delivery_Note_%s.pdf" % delivery_person_name
                content = "inline; filename='%s'" % (filename)
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename='%s'" % (filename)
                response['Content-Disposition'] = content
                return response

            return HttpResponse("Not found")


class SuppliersList(APIView):
    def get(self, request):
        try:
            delivery_person = self.request.query_params.get('delivery_person_id')
            date = self.request.query_params.get('date')
            supplier_payment_status = self.request.query_params.get('supplier_payment_status')

            purchase_date = datetime.datetime.strptime(date, "%d-%m-%Y").date().strftime("%Y-%m-%d")

            DeliveryPerson.objects.get(id=delivery_person)
            order_detail = OrderDetail.objects.filter(Q(status='purchased') | Q(status='delivered'), delivery_person=delivery_person,
                                                      order_products__purchase_details_submission_datetime__date=purchase_date, order_products__supplier_payment_status=supplier_payment_status).values(
                                                      supplier_payment_status=F('order_products__supplier_payment_status'), invoice_number=F('order_products__supplier_invoice_number'), supplier_name=F('order_products__supplier__supplier'))\
                                                      .annotate(supplier=F('order_products__supplier'), amount=Sum(F('order_products__unit_sale_price') * F('order_products__quantity'), output_field=FloatField()), datetime=F('order_products__purchase_details_submission_datetime'))

            # , product = F('order_products__product'), quantity = F('order_products__quantity'),
            # purchased_quantity = F('order_products__purchased_quantity'),
            response_list = []
            print(order_detail)
            for od in order_detail:
                print(od)
                order_prod = OrderProduct.objects.filter(purchase_details_submission_datetime__date=purchase_date, supplier_payment_status=supplier_payment_status, supplier=od['supplier'])\
                    .values('supplier_payment_status', 'supplier_invoice_number', 'unit_purchase_price', 'portrage_price', 'profit_margin'
                            ,'profit_margin_choice', 'unit_sale_price').annotate(product_name=F('product__name'), quantity_total=Sum('quantity'), purchased_quantity_total=Sum('purchased_quantity'), datetime=F('purchase_details_submission_datetime'))

                # order_prod.amount = order_prod.aggregate(amount=Sum(F('unit_sale_price') * F('quantity'), output_field=FloatField()))
                print(order_prod)
                serializer = SuppliersListSerializer(od)
                response = serializer.data
                print(order_prod)
                serializer1 = SuppliersOrderedProductsDetailSerializer(order_prod, many=True)
                # serializer1.data['quantity_sum'] = order_prod['quantity_sum']
                response['order_products'] = serializer1.data
                response_list.append(response)
            # , purchased_quantity=Sum(F('purchased_quantity')), quantity=Sum(F('quantity')), unit_purchase_price=Sum(F('unit_purchase_price')), portrage_price=Sum(F('portrage_price'))
            # , purchase_details_submission_datetime=obj['datetime']
            # print(serializer.data)
            # list_of_ordered_products = []
            # response = []
            # list_of_order_prod = []
            # for obj in serializer.data:
            #     order_prod = OrderProduct.objects.filter(supplier=obj['supplier'], supplier_invoice_number=obj['invoice_number'], supplier_payment_status=obj['supplier_payment_status'])
            #     list_of_order_prod.append(order_prod)
            # for obj1 in list_of_order_prod:
            #     list_of_ordered_products.append({'product_name': obj1.product.name, 'unit_purchase_price': obj1.unit_purchase_price,
            #                                     'portrage_price': obj1.portrage_price, 'quantity': obj1.quantity, 'purchased_quantity': obj1.purchased_quantity})
            #     obj['order_products'] = list_of_ordered_products
            #     response.append(obj)
            # OrderProduct.objects.filter()
            print(response_list)
            return Response(status=status.HTTP_200_OK, data=response_list)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': e.args})


class SubmitPurchasePaymentDetails(APIView):
    def post(self, request):
        try:
            delivery_person_id = request.data['delivery_person']
            supplier = request.data['supplier']
            # amount = request.data['amount']
            invoice_number = request.data['invoice_number']
            purchase_datetime = request.data['purchase_datetime']

            order_detail = OrderDetail.objects.filter(order_products__purchase_details_submission_datetime=purchase_datetime, delivery_person=delivery_person_id, order_products__supplier=supplier).values(order_product=F('order_products'))
            print(order_detail)

            for order_prod in order_detail:
                order_product = OrderProduct.objects.get(id=order_prod['order_product'])
                order_product.supplier_payment_status='paid'
                order_product.supplier_invoice_number=invoice_number
                order_product.payment_datetime=datetime.datetime.now()
                order_product.save()


            return Response(status=status.HTTP_200_OK, data={
                                                                'message': 'Purchase Payment details successfully submitted',
                                                            })

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': e})


class SupplierPayment(APIView):
    def post(self, request):
        try:
            invoice_number = request.data['invoice_number']
            order_products = request.data['order_products']

            for order_prod in order_products:
                payment_datetime = datetime.datetime.now()
                op = OrderProduct.objects.filter(id=order_prod['id']).update(supplier_payment_status='paid', payment_datetime=payment_datetime, invoice_number=invoice_number)
                print(op)
            return Response(status=status.HTTP_200_OK, data={'message': 'Successful'})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': e.args})