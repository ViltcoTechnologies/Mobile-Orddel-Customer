# Generated by Django 3.1.5 on 2021-01-28 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryperson',
            name='package',
        ),
    ]