# Generated by Django 5.0.2 on 2024-03-12 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driverapp', '0011_taxibooking_total_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('feedback', models.TextField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='driverapp.profiledb')),
            ],
        ),
    ]
