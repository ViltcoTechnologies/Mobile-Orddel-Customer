# Generated by Django 3.1.4 on 2021-01-29 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0005_auto_20210129_0544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientapprovallog',
            old_name='approval_status',
            new_name='admin_approval_status',
        ),
    ]
