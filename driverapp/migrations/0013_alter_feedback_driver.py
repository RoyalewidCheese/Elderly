# Generated by Django 5.0.2 on 2024-03-12 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driverapp', '0012_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='driver',
            field=models.CharField(max_length=100),
        ),
    ]
