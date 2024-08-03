# Generated by Django 5.0.7 on 2024-07-23 00:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=12)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
