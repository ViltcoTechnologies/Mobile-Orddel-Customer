from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"


class DeliveryNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryNote
        fields = "__all__"


class CreatePaymentMethodSerializer(serializers.Serializer):
    card_number = serializers.IntegerField(write_only=True)
    cvc = serializers.IntegerField(write_only=True)
    expiry_date = serializers.DateField(format="%m/%Y", input_formats=['%m/%Y'], write_only=True)


class SaveStripInfoSerializer(serializers.Serializer):
    card_number = serializers.IntegerField(write_only=True)
    cvc = serializers.IntegerField(write_only=True)
    expiry_date = serializers.DateField(format="%m/%Y", input_formats=['%m/%Y'], write_only=True)
    id = serializers.IntegerField(write_only=True)
    user_type = serializers.CharField(write_only=True)


class MakePaymentSerializer(serializers.Serializer):
    user_id = serializers.CharField(write_only=True)
    user_type = serializers.CharField(write_only=True)
    package_id = serializers.IntegerField(write_only=True)


class SuppliersListSerializer(serializers.Serializer):
    supplier = serializers.CharField(read_only=True)
    supplier_name = serializers.CharField(read_only=True)
    amount = serializers.CharField(read_only=True)
    portrage_price_total = serializers.FloatField(read_only=True)
    supplier_payment_status = serializers.CharField(read_only=True)
    invoice_number = serializers.CharField(read_only=True)
    datetime = serializers.DateTimeField(read_only=True)


class SuppliersOrderedProductsDetailSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    product_name = serializers.CharField(read_only=True)
    # quantity_total = serializers.IntegerField(read_only=True)
    purchased_quantity_total = serializers.IntegerField(read_only=True)
    purchase_price_per_unit = serializers.FloatField(read_only=True)
    portrage_price_per_unit = serializers.FloatField(read_only=True)
    # unit_sale_price = serializers.FloatField(read_only=True)
    # datetime = serializers.DateTimeField(read_only=True)
    # profit_margin = serializers.FloatField(read_only=True)
    unit_portrage_price_total = serializers.FloatField(read_only=True)
    unit_purchase_price_total = serializers.FloatField(read_only=True)
    # supplier_invoice_number = serializers.CharField(read_only=True)
    # supplier_payment_status = serializers.CharField(read_only=True)
    # profit_margin_choice = serializers.CharField(read_only=True)
    # amount = serializers.FloatField(read_only=True)
