# Generated by Django 5.0.3 on 2024-04-02 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_remove_product_ssize'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
