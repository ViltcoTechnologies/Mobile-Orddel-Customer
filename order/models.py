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
    ('rejected', 'Rejected'),
    ('in_progress', 'In Progress'),
    ('purchased', 'Purchased'),
    ('delivered', 'Delivered')

)
supplier_payment_choices = (
    ('paid', 'Paid'),
    ('unpaid', 'Unpaid')

)

cart_staging_choices = (
    ('staged', 'Staged'),
    ('unstaged', 'Unstaged')

)

profit_choices = (
    ('percentage', 'Percentage'),
    ('value', 'Value')

)


class OrderBox(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    # grand_total = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.id)


class Supplier(models.Model):
    supplier = models.CharField(max_length=30, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class OrderProduct(models.Model):
    order_box = models.ForeignKey(OrderBox, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    purchased_quantity = models.IntegerField(default=0)
    total_amount = models.FloatField(default=0.0)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    supplier_payment_status = models.CharField(choices=supplier_payment_choices, max_length=50, null=True, blank=True, default=supplier_payment_choices[1][1])
    supplier_invoice_number = models.CharField(max_length=500, null=True, blank=True)
    purchase_details_submission_datetime = models.DateTimeField(auto_now=False, null=True, blank=True)
    payment_datetime = models.DateTimeField(auto_now=False, null=True, blank=True)
    unit_purchase_price = models.FloatField(default=0.0)
    portrage_price = models.FloatField(default=0.0, null=True, blank=True)
    profit_margin = models.FloatField(default=0.0)
    profit_margin_choice = models.CharField(max_length=100, choices=profit_choices, null=True, blank=True)
    unit_sale_price = models.FloatField(default=0.0)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class OrderDetail(models.Model):
    order_box = models.ForeignKey(OrderBox, on_delete=models.SET_NULL, null=True, blank=True)
    business = models.ForeignKey(ClientBusinessDetail, on_delete=models.SET_NULL, null=True, blank=True)
    order_products = models.ManyToManyField(OrderProduct)
    # Unique Purchase Order Number assigned to client on every order
    purchase_order_no = models.CharField(max_length=100)
    order_title = models.CharField(max_length=100, null=True, blank=True)
    delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.SET_NULL, null=True, blank=True)
    order_created_datetime = models.DateTimeField(auto_now=True)
    order_delivery_datetime = models.DateTimeField(auto_now=False)
    # shipment_address = models.ForeignKey(ClientShipmentAddress, on_delete=models.SET_NULL, null=True, blank=True)
    delivery_notes = models.TextField(max_length=1000, null=True, blank=True)
    comment = models.TextField(max_length=500, null=True, blank=True)
    distance = models.CharField(max_length=100, null=True, blank=True)
    # total_units_ordered = models.IntegerField(default=0)
    status = models.CharField(max_length=100, choices=order_status_choices, null=True, blank=True)
    payment_type = models.CharField(max_length=100, choices=payment_choices, null=True, blank=True)

    def __str__(self):
        return str(self.id)

