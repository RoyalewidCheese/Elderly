# Generated by Django 5.0.2 on 2024-03-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosapp', '0005_prescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='total_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
