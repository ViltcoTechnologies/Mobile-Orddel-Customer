# Generated by Django 3.1.4 on 2021-01-04 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_app', '0006_auto_20210104_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryperson',
            name='buying_capacity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='deliveryperson',
            name='total_amount_shopped',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
