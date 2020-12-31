from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = "__all__"
