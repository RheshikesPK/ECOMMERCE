# Generated by Django 5.0.3 on 2024-08-26 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_orderitem_total_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderPayment',
        ),
    ]
