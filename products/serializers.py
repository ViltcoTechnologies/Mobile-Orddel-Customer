from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


# class VehicleRegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = VehicleRegistration
#         fields = "__all__"
#
#
# class InvoiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Invoice
#         fields = "__all__"
