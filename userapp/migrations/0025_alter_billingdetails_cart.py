# Generated by Django 5.0.2 on 2024-03-27 05:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0024_alter_billingdetails_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingdetails',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.cartitem'),
        ),
    ]
