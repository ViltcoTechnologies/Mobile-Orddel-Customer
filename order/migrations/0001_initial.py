# Generated by Django 2.2.7 on 2021-04-29 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '__first__'),
        ('client_app', '__first__'),
        ('delivery_app', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client_app.Client')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('purchased_quantity', models.IntegerField(default=0)),
                ('total_amount', models.FloatField(default=0.0)),
                ('supplier', models.CharField(blank=True, max_length=30, null=True)),
                ('supplier_payment_status', models.CharField(blank=True, choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], default='Unpaid', max_length=50, null=True)),
                ('supplier_invoice_number', models.CharField(blank=True, max_length=500, null=True)),
                ('payment_datetime', models.DateTimeField(blank=True, null=True)),
                ('unit_purchase_price', models.FloatField(default=0.0)),
                ('portrage_price', models.FloatField(blank=True, default=0.0, null=True)),
                ('profit_margin', models.FloatField(default=0.0)),
                ('profit_margin_choice', models.CharField(blank=True, choices=[('percentage', 'Percentage'), ('value', 'Value')], max_length=100, null=True)),
                ('unit_sale_price', models.FloatField(default=0.0)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('order_box', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.OrderBox')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_order_no', models.CharField(max_length=100)),
                ('order_title', models.CharField(blank=True, max_length=100, null=True)),
                ('order_created_datetime', models.DateTimeField(auto_now=True)),
                ('order_delivery_datetime', models.DateTimeField()),
                ('delivery_notes', models.TextField(blank=True, max_length=1000, null=True)),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('distance', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, choices=[('pending', 'Pending'), ('rejected', 'Rejected'), ('in_progress', 'In Progress'), ('purchased', 'Purchased'), ('delivered', 'Delivered')], max_length=100, null=True)),
                ('payment_type', models.CharField(blank=True, choices=[('cash_on_delivery', 'Cash On Delivery'), ('online_payment', 'Online Payment')], max_length=100, null=True)),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client_app.ClientBusinessDetail')),
                ('delivery_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='delivery_app.DeliveryPerson')),
                ('order_box', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.OrderBox')),
                ('order_products', models.ManyToManyField(to='order.OrderProduct')),
            ],
        ),
    ]
