from django.contrib import admin
from .models import *


class VersionControlAdmin(admin.ModelAdmin):
    list_display = ('apk_version', 'date_created')
    list_display_links = ('apk_version', 'date_created')


admin.site.register(VersionControl, VersionControlAdmin)
