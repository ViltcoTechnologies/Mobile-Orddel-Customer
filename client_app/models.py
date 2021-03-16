from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from . import *
from delivery_app.models import *


# Choices menu
gender_choices = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')

    )

package_activation_choices = (
    ('inactive', 'Inactive'),
    ('active', 'Active')

)

admin_approval_choices = (
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('unapproved', 'Unapproved'),
    ('cancelled', 'Cancelled')
)

# business_choices = (
#     ('shop', 'Shop'),
#     ('restaurant', 'Restaurant'),
#     ('catering', 'Catering')
#     )

# business_type_choices = (
#     ('online', 'Online'),
#     ('physical', 'Physical')
#     )


class ClientPackage(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, null=True, blank=True)
    no_of_invoices = models.IntegerField(default=0)
    validity_in_days = models.IntegerField(default=0)
    price = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Client registered
class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    preferred_delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.SET_NULL, null=True, blank=True)
    package = models.ForeignKey(ClientPackage, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=300)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200, null=True, blank=True)
    current_location = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=300, choices=gender_choices, blank=True, null=True)
    image = models.ImageField(upload_to=f"clients/photos/", null=True, blank=True)
    number_of_order = models.IntegerField(default=0)
    total_amount_shopped = models.IntegerField(default=0)
    no_of_invoices = models.IntegerField(default=0)
    otp_status = models.BooleanField(default=False)
    admin_approval_status = models.CharField(max_length=100, choices=admin_approval_choices)
    approval_read_status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class ClientPackageLog(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    package = models.ForeignKey(ClientPackage, on_delete=models.SET_NULL, null=True, blank=True)
    date_activated = models.DateField(auto_now=True)
    status = models.CharField(max_length=100, choices=package_activation_choices)

    def __str__(self):
        return self.id


# Client can have multiple businesses
class ClientBusinessDetail(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    nature = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to=f"business/logo/", null=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Client can have many shipment addresses
class ClientShipmentAddress(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    shipment_address = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shipment_address


# Client can have multiple bank accounts
class ClientBankDetail(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    branch_code = models.CharField(max_length=100, null=True, blank=True)
    card_no = models.CharField(max_length=150, null=True, blank=True)
    sort_code = models.CharField(max_length=10, null=True, blank=True)
    credit_card_expiry = models.DateField(auto_now=False, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bank_name


