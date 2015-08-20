# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('institutions', '0002_auto_20150820_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('address', models.ForeignKey(to='core.Address', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(to='events.EventType'),
        ),
        migrations.AddField(
            model_name='event',
            name='institute',
            field=models.ForeignKey(to='institutions.Institute'),
        ),
    ]
