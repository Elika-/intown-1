# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150825_1909'),
        ('institutions', '0003_auto_20150825_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstituteOpenHours',
            fields=[
                ('openhours_ptr', models.OneToOneField(auto_created=True, primary_key=True, to='core.OpenHours', serialize=False, parent_link=True)),
            ],
            bases=('core.openhours',),
        ),
        migrations.RemoveField(
            model_name='institute',
            name='open_hours',
        ),
        migrations.AddField(
            model_name='instituteopenhours',
            name='institute_fk',
            field=models.ForeignKey(to='institutions.Institute'),
        ),
    ]
