from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToCart
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = "__all__"


class ConsolidatedPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsolidatedPurchase
        fields = "__all__"
