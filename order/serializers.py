from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class OrderBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBox
        fields = "__all__"


class OrderProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        exclude = ('order_products',)


class ConsolidatedPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsolidatedPurchase
        fields = "__all__"
