# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Name', models.CharField(max_length=50)),
                ('Place', models.CharField(max_length=50)),
                ('PhoneNumber', models.CharField(max_length=15)),
                ('CarBrand', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('emailid', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Imagename', models.CharField(max_length=50)),
                ('Image', models.ImageField(upload_to='media/Gallery')),
            ],
        ),
    ]
