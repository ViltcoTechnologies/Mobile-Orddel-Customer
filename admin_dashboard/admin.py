from django.contrib import admin
from .models import *


class AdminUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'phone_number',
                    'gender', 'date_created')
    list_display_links = ('first_name',)


admin.site.register(AdminUser, AdminUserAdmin)
