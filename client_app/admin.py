from django.contrib import admin
from .models import *


class ClientUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'phone_number',
                    'gender', 'date_created')
    list_display_links = ('first_name', 'last_name', 'username', 'email')


admin.site.register(Client, ClientUserAdmin)

class BusinessDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'name', 'nature', 'type', 'logo', 'date_created')
    list_display_links = ('name', 'nature', 'type')


admin.site.register(BusinessDetail, BusinessDetailAdmin)

class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'shipment_address', 'date_created')
    list_display_links = ('client', 'date_created')


admin.site.register(ShipmentAddress, ShipmentAdmin)

class BankDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'bank_name', 'branch_code', 'date_created')
    list_display_links = ('id', 'bank_name')


admin.site.register(BankDetails, BankDetailsAdmin)

class PackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'date_created')
    list_display_links = ('id', 'name')


admin.site.register(Package, PackageAdmin)




