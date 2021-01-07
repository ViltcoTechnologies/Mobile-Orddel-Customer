# Generated by Django 3.1.4 on 2021-01-05 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_app', '0013_auto_20210105_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='company_name',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='vehicle_name',
            new_name='make',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='copy_image_back',
            field=models.ImageField(blank=True, null=True, upload_to='vehicle/photos/<built-in function id>/'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='copy_image_front',
            field=models.ImageField(blank=True, null=True, upload_to='vehicle/photos/<built-in function id>/'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='model',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='year',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
