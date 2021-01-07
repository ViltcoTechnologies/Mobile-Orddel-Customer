from django.contrib import admin
from .models import *


class DeliveryPersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'phone_number',
                    'no_of_orders', 'buying_capacity', 'gender', 'date_created')
    list_display_links = ('first_name', 'last_name', 'username', 'email')


admin.site.register(DeliveryPerson, DeliveryPersonAdmin)


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'delivery_person', 'make', 'model', 'color', 'year', 'registration_no',
                    'date_created')
    list_display_links = ('delivery_person', 'make')


admin.site.register(Vehicle, VehicleAdmin)
