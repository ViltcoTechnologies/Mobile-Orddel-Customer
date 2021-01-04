from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class BusinessDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessDetail
        fields = "__all__"


class ShipmentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentAddress
        fields = "__all__"


class BankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetails
        fields = "__all__"

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = "__all__"
