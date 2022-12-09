from django.contrib import admin
from .models import *


class AdminUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'phone_number',
                    'gender', 'date_created')
    list_display_links = ('first_name',)


admin.site.register(AdminUser, AdminUserAdmin)


class ClientApprovalLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'admin', 'admin_approval_status', 'date_created')
    list_display_links = ('client',)


admin.site.register(ClientApprovalLog, ClientApprovalLogAdmin)


class DeliveryPersonApprovalLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'delivery_person', 'admin', 'admin_approval_status', 'date_created')
    list_display_links = ('delivery_person',)


admin.site.register(DeliveryPersonApprovalLog, DeliveryPersonApprovalLogAdmin)
