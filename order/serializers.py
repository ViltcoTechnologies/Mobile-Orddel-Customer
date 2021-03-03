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
    business_address = serializers.CharField(source='business.address')
    business_name = serializers.CharField(source='business.name')
    order_delivery_datetime = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S.%f%z", input_formats=['%d-%m-%Y %H:%M:%S.%f%z', 'iso-8601'])
    class Meta:
        model = OrderDetail
        exclude = ('order_products',)


class ConsolidatedPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsolidatedPurchase
        fields = "__all__"


# class InsertConsolidatePurchaseDetailsSerializer(serializers.Serializer):
#     class Meta:
#         fields = "delivery_person_id, product_id, supplier, unit_purchase_price, profit_margin"
