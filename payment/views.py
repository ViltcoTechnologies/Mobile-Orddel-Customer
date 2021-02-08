from django.shortcuts import render
from rest_framework import status, generics, permissions
from .models import *
from .serializers import *
# Create your views here.


class ListCreateInvoice(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
