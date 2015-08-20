# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('address_line_1', models.CharField(max_length=100)),
                ('address_line_2', models.CharField(null=True, blank=True, max_length=100)),
                ('zip_code', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=60)),
                ('lat', models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=4)),
                ('lng', models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=4)),
                ('phone', models.CharField(null=True, blank=True, max_length=25)),
                ('email', models.EmailField(null=True, blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('iso3166', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(to='core.Country'),
        ),
    ]
