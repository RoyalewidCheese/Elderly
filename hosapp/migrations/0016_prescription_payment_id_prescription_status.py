# Generated by Django 5.0.2 on 2024-03-27 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosapp', '0015_delete_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='payment_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='prescription',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('success', 'Success')], default='pending', max_length=20),
        ),
    ]
