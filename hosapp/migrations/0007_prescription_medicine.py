# Generated by Django 5.0.2 on 2024-03-22 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosapp', '0006_alter_prescription_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='medicine',
            field=models.TextField(null=True),
        ),
    ]
