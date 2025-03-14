# Generated by Django 5.0.2 on 2024-03-04 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(blank=True, max_length=100, null=True)),
                ('LastName', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Location', models.CharField(blank=True, max_length=100, null=True)),
                ('Timefrom', models.TimeField(blank=True, max_length=100, null=True)),
                ('Timeto', models.TimeField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
