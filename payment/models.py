from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from client_app.models import *
from order.models import *
from delivery_app.models import *


class DeliveryNote(models.Model):
    order = models.ForeignKey(OrderDetail, on_delete=models.CASCADE, null=True, blank=True)
    do_number = models.CharField(max_length=100, null=True, blank=True)
    delivery_note = models.CharField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Invoice(models.Model):
    order = models.ForeignKey(OrderDetail, on_delete=models.SET_NULL, null=True, blank=True)
    inv_number = models.CharField(max_length=100, null=True, blank=True)
    total_amount = models.FloatField(default=0.0)
    date_created = models.DateTimeField(auto_now=True)
    # client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    # delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.SET_NULL, null=True, blank=True)
    # delivery_note = models.ForeignKey(DeliveryNote, on_delete=models.SET_NULL, null=True, blank=True)
    # subtotal = models.FloatField(default=0.0)
    # portrage_price = models.FloatField(default=0.0)
    # profit = models.FloatField(default=0.0)
    # total = models.FloatField(default=0.0)
    # sales_price = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.id)


class ItemUnitPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    unit_price = models.IntegerField(default=0.0)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class ClientPaymentDetails(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=100)
    payment_method_id = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)


class DeliveryPaymentDetails(models.Model):
    delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=50)
    payment_method_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
