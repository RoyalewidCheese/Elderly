# Generated by Django 5.0.2 on 2024-03-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_remove_contactdb_lastname'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Groceryname', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
