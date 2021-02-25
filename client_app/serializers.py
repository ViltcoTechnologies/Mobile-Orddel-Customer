from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class BusinessDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientBusinessDetail
        fields = "__all__"
        lookup_field = 'client'


class ShipmentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientShipmentAddress
        fields = "__all__"


class BankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientBankDetail
        fields = "__all__"


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientPackage
        fields = "__all__"
