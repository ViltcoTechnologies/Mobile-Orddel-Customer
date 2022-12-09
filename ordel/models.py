from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

app_label = 'ordel'


class VersionControl(models.Model):
    apk_version = models.FloatField(default=0)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)