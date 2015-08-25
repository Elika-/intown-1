# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150825_1829'),
        ('institutions', '0002_auto_20150820_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='openhours',
            name='institute',
        ),
        migrations.AddField(
            model_name='institute',
            name='open_hours',
            field=models.ForeignKey(null=True, to='core.OpenHours'),
        ),
        migrations.DeleteModel(
            name='OpenHours',
        ),
    ]
