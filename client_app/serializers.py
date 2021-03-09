from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class ClientImageSerializer(serializers.Serializer):
    client_id = serializers.IntegerField(required=True)
    image = serializers.ImageField(required=True)

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('client_id', instance.email)
        instance.image = validated_data.get('image', instance.content)
        instance.save()

        Client.objects.filter(id=instance.id).update(image=instance.image)
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


