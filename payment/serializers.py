from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"

