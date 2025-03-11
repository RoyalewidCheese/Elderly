# Generated by Django 5.0.2 on 2024-03-27 05:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0019_alter_billingdetails_cart_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingdetails',
            name='cart_item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='billing_details', to='userapp.cartitem'),
        ),
    ]
