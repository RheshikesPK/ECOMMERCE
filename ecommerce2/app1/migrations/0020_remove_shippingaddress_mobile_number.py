# Generated by Django 5.0.3 on 2024-09-09 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_alter_shippingaddress_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='mobile_number',
        ),
    ]
