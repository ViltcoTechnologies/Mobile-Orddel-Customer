# Generated by Django 3.1.4 on 2021-01-05 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_app', '0012_auto_20210105_0735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='model',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='license_image_back',
            field=models.ImageField(blank=True, null=True, upload_to='vehicle/photos/<built-in function id>/'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='license_image_front',
            field=models.ImageField(blank=True, null=True, upload_to='vehicle/photos/<built-in function id>/'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='license_no',
            field=models.ImageField(blank=True, null=True, upload_to='vehicle/photos/<built-in function id>/'),
        ),
    ]
