# Generated by Django 3.1.4 on 2020-12-31 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminuser',
            name='current_location',
        ),
        migrations.RemoveField(
            model_name='adminuser',
            name='shipment_address',
        ),
        migrations.AddField(
            model_name='adminuser',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
