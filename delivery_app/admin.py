from django.contrib import admin
from .models import *


class DeliveryPersonPackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'date_created')
    list_display_links = ('id', 'name')


admin.site.register(DeliveryPersonPackage, DeliveryPersonPackageAdmin)


class DeliveryPersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'phone_number',
                    'no_of_orders', 'buying_capacity', 'package', 'date_created',
                    'otp_status', 'admin_approval_status', 'no_of_active_order')
    list_display_links = ('first_name', 'package')


admin.site.register(DeliveryPerson, DeliveryPersonAdmin)


class DeliveryPersonBusinessDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'delivery_person', 'name', 'nature', 'type', 'logo', 'date_created')
    list_display_links = ('name', 'nature', 'type')


admin.site.register(DeliveryPersonBusinessDetail, DeliveryPersonBusinessDetailAdmin)


class DeliveryPersonBankDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'delivery_person', 'bank_name', 'account_title', 'sort_code', 'date_created')
    list_display_links = ('id', 'bank_name')


admin.site.register(DeliveryPersonBankDetail, DeliveryPersonBankDetailAdmin)


class DeliveryPersonPackageLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'delivery_person', 'package', 'date_activated', 'status')
    list_display_links = ('id', 'delivery_person', 'package')


admin.site.register(DeliveryPersonPackageLog, DeliveryPersonPackageLogAdmin)


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'delivery_person', 'make', 'model', 'color', 'year', 'registration_no',
                    'date_created')
    list_display_links = ('delivery_person',)


admin.site.register(Vehicle, VehicleAdmin)


