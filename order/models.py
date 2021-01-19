from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from client_app.models import *
from delivery_app.models import *
from products.models import *

payment_choices = (
    ('cash_on_delivery', 'Cash On Delivery'),
    ('online_payment', 'Online Payment')

)

order_status_choices = (
    ('pending', 'Pending'),
    ('delivered', 'Delivered')

)


class Cart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    grand_total = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.id)


class CartProducts(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    total_amount = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.id)


class OrderDetail(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    cart_products = models.ForeignKey(CartProducts, on_delete=models.SET_NULL, null=True, blank=True)
    purchase_order_no = models.CharField(max_length=100) # Unique Purchase Order Number assigned to client on every order
    order_title = models.CharField(max_length=100, null=True, blank=True)
    delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.SET_NULL, null=True, blank=True)
    order_created_datetime = models.DateTimeField(auto_now=True)
    order_delivery_datetime= models.DateTimeField(auto_now=False)
    shipment_address = models.ForeignKey(ShipmentAddress, on_delete=models.SET_NULL, null=True, blank=True)
    delivery_notes = models.TextField(max_length=1000, null=True, blank=True)
    comment = models.TextField(max_length=500, null=True, blank=True)
    distance = models.CharField(max_length=100, null=True, blank=True)
    total_units_ordered = models.IntegerField(default=0)
    status = models.CharField(max_length=100, choices = order_status_choices, null=True, blank=True)
    payment_type = models.CharField(max_length=100, choices = payment_choices, null=True, blank=True)

    def __str__(self):
        return self.order_title

