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
    amount = serializers.CharField(read_only=True)
    supplier_payment_status = serializers.CharField(read_only=True)