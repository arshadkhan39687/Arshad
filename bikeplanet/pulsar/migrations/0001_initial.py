# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bikes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bike_name', models.CharField(max_length=15)),
                ('launch_date', models.CharField(max_length=20)),
                ('bike_desc', models.CharField(max_length=500)),
                ('review', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Next',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bike_name', models.CharField(max_length=15)),
                ('launch_date', models.CharField(max_length=20)),
                ('bike_desc', models.CharField(max_length=500)),
                ('review', models.CharField(max_length=250)),
            ],
        ),
    ]
