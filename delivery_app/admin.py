from django.contrib import admin
from .models import *


class DeliveryPersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'phone_number',
                    'no_of_orders', 'buying_capacity', 'gender', 'date_created')
    list_display_links = ('first_name', 'last_name', 'username', 'email')


admin.site.register(DeliveryPerson, DeliveryPersonAdmin)


class VehicleRegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'delivery_person', 'vehicle_name', 'company_name', 'model', 'registration_no',
                    'year_registered')
    list_display_links = ('delivery_person', 'vehicle_name', 'company_name')


admin.site.register(VehicleRegistration, VehicleRegistrationAdmin)
