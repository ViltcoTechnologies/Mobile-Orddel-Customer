# Generated by Django 3.1.4 on 2021-01-21 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client_app', '0001_initial'),
        ('delivery_app', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vat', models.FloatField(default=0.2)),
                ('portrage_price', models.FloatField(default=0.0)),
                ('profit', models.FloatField(default=0.0)),
                ('sales_price', models.FloatField(default=0.0)),
                ('item', models.FloatField(default=0.0)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('delivery_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='delivery_app.deliveryperson')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.orderdetail')),
                ('payment_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client_app.client')),
            ],
        ),
    ]
