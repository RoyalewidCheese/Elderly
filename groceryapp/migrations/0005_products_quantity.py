# Generated by Django 5.0.2 on 2024-03-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0004_rename_storename_products_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='Quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
