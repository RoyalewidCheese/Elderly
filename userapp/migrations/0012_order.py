# Generated by Django 5.0.2 on 2024-03-19 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0011_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('town', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
