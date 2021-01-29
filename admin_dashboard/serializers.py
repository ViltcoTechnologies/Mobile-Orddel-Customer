from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = "__all__"


class ClientApprovalLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientApprovalLog
        fields = "__all__"


class DeliveryPersonApprovalLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPersonApprovalLog
        fields = "__all__"
