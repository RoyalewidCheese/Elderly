# Generated by Django 5.0.2 on 2024-03-19 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_cartitem_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='total_price',
            new_name='original_price',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='image',
            field=models.ImageField(null=True, upload_to='product_images/'),
        ),
    ]
