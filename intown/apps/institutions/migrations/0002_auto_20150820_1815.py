# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '__first__'),
        ('institutions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institute',
            name='address_line_1',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='address_line_2',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='city',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='country',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='state',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='institute',
            name='address',
            field=models.ForeignKey(null=True, to='core.Address'),
        ),
    ]
