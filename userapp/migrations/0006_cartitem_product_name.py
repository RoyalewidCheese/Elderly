# Generated by Django 5.0.2 on 2024-03-19 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='product_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
