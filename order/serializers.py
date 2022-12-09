from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from payment.models import *
from payment.serializers import *


class OrderBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBox
        fields = "__all__"


class OrderProductsSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderProduct
        fields = "__all__"


class RelatedFieldAlternative(serializers.PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = kwargs.pop('serializer', None)
        if self.serializer is not None and not issubclass(self.serializer, serializers.Serializer):
            raise TypeError('"serializer" is not a valid serializer class')

        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False if self.serializer else True

    def to_representation(self, instance):
        if self.serializer:
            return self.serializer(instance, context=self.context).data
        return super().to_representation(instance)

class OrderDetailSerializer(serializers.ModelSerializer):
    business_address = serializers.CharField(source='business.address', read_only=True)
    business_name = serializers.CharField(source='business.name', read_only=True)
    # invoice = RelatedFieldAlternative(queryset=Invoice.objects.all(), serializer=InvoiceSerializer)
    order_delivery_datetime = serializers.DateTimeField(format="%d-%m-%Y %H:%M", input_formats=['%d-%m-%Y %H:%M:%S.%f%z', 'iso-8601'])
    class Meta:
        model = OrderDetail
        exclude = ('order_products',)


# class InsertConsolidatePurchaseDetailsSerializer(serializers.Serializer):
#     class Meta:
#         fields = "delivery_person_id, product_id, supplier, unit_purchase_price, profit_margin"
