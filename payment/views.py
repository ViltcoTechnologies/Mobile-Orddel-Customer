from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date
from .models import *
from .serializers import *
# Create your views here.


class GetInvNumberAPIView(APIView):

    def get(self, request, id=None):
        if id:
            # try:
            invoice = Invoice.objects.get(order=id)
            orderdetail = OrderDetail.objects.get(id=id)
            delivery_person = orderdetail.delivery_person.id
            if invoice:
                inv_number_list = invoice.inv_number.split("_")
                inv_number = int(inv_number_list[2])
                inv_number += 1
                invoice_order_no = f"PO#{str(delivery_person).zfill(5)}_{date.today().strftime('%Y')}_{str(inv_number).zfill(5)}"
            else:
                inv_number = 1
                invoice_order_no = f"PO#{str(delivery_person).zfill(5)}_{date.today().strftime('%Y')}_{str(inv_number).zfill(5)}"

            # except:
            #     return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "order not found"})

            return Response(status=status.HTTP_200_OK, data={"invoice_number": invoice_order_no})

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "id not provided"})


class ListCreateInvoice(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


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


class CreateDeliveryNote(generics.CreateAPIView):
    queryset = DeliveryNote.objects.all()
    serializer_class = DeliveryNoteSerializer
