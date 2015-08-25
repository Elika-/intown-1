# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_remove_event_open_hours'),
        ('core', '0004_auto_20150825_1909'),
        ('institutions', '0005_auto_20150825_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instituteaddress',
            name='address_ptr',
        ),
        migrations.RemoveField(
            model_name='instituteaddress',
            name='institute_fk',
        ),
        migrations.AddField(
            model_name='institute',
            name='address',
            field=models.ForeignKey(null=True, to='core.Address'),
        ),
        migrations.DeleteModel(
            name='InstituteAddress',
        ),
    ]
