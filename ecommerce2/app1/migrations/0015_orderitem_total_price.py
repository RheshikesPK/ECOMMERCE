# Generated by Django 5.0.3 on 2024-08-20 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_orderpayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
