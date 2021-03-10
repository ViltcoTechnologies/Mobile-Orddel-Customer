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


class DeliveryPersonImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    image = serializers.ImageField(required=True)

    class Meta:
        model = DeliveryPerson
        fields = ("id", "image")

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.image = validated_data.get("image", instance.image)
        instance.save()
        return instance


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


