from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class ClientImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    image = serializers.ImageField(required=True)

    class Meta:
        model = Client
        fields = ("id", "image")

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.image = validated_data.get("image", instance.image)
        instance.save()
        return instance


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


