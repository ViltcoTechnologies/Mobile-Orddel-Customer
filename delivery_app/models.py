from django.db import models
from django.contrib.auth.models import User
from products.models import *


gender_choices = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
)

admin_approval_choices = (
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('unapproved', 'Unapproved'),
    ('cancelled', 'Cancelled')
)

package_activation_choices = (
    ('inactive', 'Inactive'),
    ('active', 'Active')

)


class DeliveryPersonPackage(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, null=True, blank=True)
    no_of_invoices = models.IntegerField(default=0)
    validity_in_days = models.IntegerField(default=0)
    price = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Delivery Person registration model
class DeliveryPerson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(DeliveryPersonPackage, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=300)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200, blank=True, null=True)
    current_location = models.CharField(max_length=100, blank=True, null=True)
    no_of_orders = models.IntegerField(default=0, blank=True, null=True)
    buying_capacity = models.IntegerField(default=0, blank=True, null=True)
    total_amount_shopped = models.IntegerField(default=0, blank=True, null=True)
    gender = models.CharField(max_length=300, choices=gender_choices, blank=True, null=True)
    image = models.ImageField(upload_to=f"delivery_person/photos/", null=True, blank=True)
    no_of_invoices = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now=True, null=True, blank=True)
    otp_status = models.BooleanField(default=False)
    admin_approval_status = models.CharField(max_length=300, choices=admin_approval_choices)
    approval_read_status = models.BooleanField(default=False)
    no_of_active_order = models.IntegerField(default=0)

    def __str__(self):
        return str(self.username)


class DeliveryPersonPackageLog(models.Model):
    delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.CASCADE)
    package = models.ForeignKey(DeliveryPersonPackage, on_delete=models.SET_NULL, null=True, blank=True)
    date_activated = models.DateField(auto_now=True)
    status = models.CharField(max_length=100, choices=package_activation_choices)

    def __str__(self):
        return self.id


# Client can have multiple businesses
class DeliveryPersonBusinessDetail(models.Model):
    delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    nature = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to=f"business/logo/", null=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Client can have multiple bank accounts
class DeliveryPersonBankDetail(models.Model):
    delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.CASCADE, null=True, blank=True)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    branch_code = models.CharField(max_length=100, null=True, blank=True)
    credit_card_no = models.CharField(max_length=150, null=True, blank=True)
    sort_code = models.CharField(max_length=10, null=True, blank=True)
    credit_card_expiry = models.DateField(auto_now=False, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bank_name


# Vehicle registration model
class Vehicle(models.Model):
    delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.CASCADE, null=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    registration_no = models.CharField(max_length=100)
    license_image_front = models.ImageField(upload_to=f"vehicle/photos/", null=True, blank=True)
    license_image_back = models.ImageField(upload_to=f"vehicle/photos/", null=True, blank=True)
    copy_image_front = models.ImageField(upload_to=f"vehicle/photos/", null=True, blank=True)
    copy_image_back = models.ImageField(upload_to=f"vehicle/photos/", null=True, blank=True)
    license_no = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


