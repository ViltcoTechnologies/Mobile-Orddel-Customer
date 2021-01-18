import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ordel.settings')

import django
django.setup()

import random

from client_app.models import *
from delivery_app.models import *
from order.models import *
from payment.models import *
from products.models import *

from faker import Faker
from faker_vehicle import VehicleProvider

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

import secrets
import string

fake = Faker()
fake.add_provider(VehicleProvider)


def populate(n):
    genders = ['male', 'female']
    # Population script loop
    for entry in range(n):

        # -----------------------------------------------------------------------------------------------------

        # Populating Client Script
        profile = fake.profile()
        package_id = random.randint(1,3)
        first_name = fake.first_name()
        last_name = fake.last_name()
        username = profile['username']
        email = profile['mail']
        # generating password ------------------------------------------
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(20))
        # --------------------------------------------------------------
        phone_number = fake.phone_number()
        address = profile['address']
        current_location = profile['current_location']
        no_of_orders = random.randint(0, 1000)
        total_amount_shopped = random.randint(0, 1000000)
        gender = random.choice(genders)
        image = 'https://cdn.artandlogic.com/wp-content/uploads/django.jpeg'
        try:
            saved_data = User.objects.get(username=username)
        except:
            new_auth_user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            new_auth_user.first_name = first_name
            new_auth_user.last_name = last_name

            package_instance = Package.objects.get(id=package_id)

            # Entering record in the Client Table
            new_client = Client.objects.create(
                user=new_auth_user,
                package=package_instance,
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                phone_number=phone_number,
                address=address,
                current_location=current_location,
                number_of_order=no_of_orders,
                total_amount_shopped=total_amount_shopped,
                gender=gender,
                image=image
            )
            new_auth_user.save()
            new_client.save()

        # -----------------------------------------------------------------------------------------------------
        # Populating Delivery Person Script
        profile = fake.profile()
        first_name = fake.first_name()
        last_name = fake.last_name()
        username = profile['username']
        email = profile['mail']
        # generating password ------------------------------------------
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(20))
        # --------------------------------------------------------------
        phone_number = fake.phone_number()
        address = profile['address']
        current_location = profile['current_location']
        no_of_orders = random.randint(0, 1000)
        buying_capacity = random.randint(0, 10000000)
        total_amount_shopped = random.randint(0, 1000000)
        gender = random.choice(genders)
        image = 'https://cdn.artandlogic.com/wp-content/uploads/django.jpeg'
        try:
            saved_data = User.objects.get(username=username)
        except:
            new_auth_user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            new_auth_user.first_name = first_name
            new_auth_user.last_name = last_name

            # Entering record in the Delivery Person Table
            new_delivery_person = DeliveryPerson.objects.create(
                user=new_auth_user,
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                phone_number=phone_number,
                address=address,
                current_location=current_location,
                no_of_orders=no_of_orders,
                buying_capacity=buying_capacity,
                total_amount_shopped=total_amount_shopped,
                gender=gender,
                image=image
            )
            new_auth_user.save()
            new_delivery_person.save()

        # -----------------------------------------------------------------------------------------------------
        # Populating Vehicle Registration Script
        make = fake.vehicle_make()
        model = fake.vehicle_model()
        color = fake.safe_color_name()
        year = fake.vehicle_year()
        registration_no = fake.license_plate()
        license_image_front = 'https://cdn.artandlogic.com/wp-content/uploads/django.jpeg'
        license_image_back = 'https://cdn.artandlogic.com/wp-content/uploads/django.jpeg'
        copy_image_front = 'https://cdn.artandlogic.com/wp-content/uploads/django.jpeg'
        copy_image_back = 'https://cdn.artandlogic.com/wp-content/uploads/django.jpeg'
        license_no = random.randint(100000000000, 999999999999)
        try:
            saved_data = Vehicle.objects.get(registration_no=registration_no)
        except:
            # Entering record in the Vehicle Table
            new_vehicle = Vehicle.objects.create(
                delivery_person=new_delivery_person,
                make=make,
                model=model,
                color=color,
                year=year,
                registration_no=registration_no,
                license_image_front=license_image_front,
                license_image_back=license_image_back,
                copy_image_front=copy_image_front,
                copy_image_back=copy_image_back,
                license_no=license_no
            )
            new_vehicle.save()


if __name__ == '__main__':
    populate(5)
