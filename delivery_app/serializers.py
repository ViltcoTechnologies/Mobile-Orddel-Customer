from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class DeliveryPersonPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPerson
        fields = "__all__"


class DeliveryPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPerson
        fields = "__all__"


class DeliveryPersonPackageLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPerson
        fields = "__all__"


class DeliveryPersonBusinessDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPerson
        fields = "__all__"


class DeliveryPersonBankDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPerson
        fields = "__all__"


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"


class ConsolidatedPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsolidatedPurchase
        fields = "__all__"
