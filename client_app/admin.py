from django.contrib import admin
from .models import *


class ClientUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'phone_number',
                    'gender', 'date_created', 'otp_status', 'admin_approval_status', 'approval_read_status')
    list_display_links = ('first_name', 'last_name', 'username', 'email')


admin.site.register(Client, ClientUserAdmin)


class ClientBusinessDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'name', 'nature', 'type', 'logo', 'date_created')
    list_display_links = ('name', 'nature', 'type')


admin.site.register(ClientBusinessDetail, ClientBusinessDetailAdmin)


class ClientShipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'shipment_address', 'date_created')
    list_display_links = ('client', 'date_created')


admin.site.register(ClientShipmentAddress, ClientShipmentAdmin)


class ClientBankDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'bank_name', 'branch_code', 'date_created')
    list_display_links = ('id', 'bank_name')


admin.site.register(ClientBankDetail, ClientBankDetailAdmin)


class ClientPackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'date_created')
    list_display_links = ('id', 'name')


admin.site.register(ClientPackage, ClientPackageAdmin)


class ClientPackageLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'package', 'date_activated', 'status')
    list_display_links = ('id', 'client', 'package')


admin.site.register(ClientPackageLog, ClientPackageLogAdmin)

