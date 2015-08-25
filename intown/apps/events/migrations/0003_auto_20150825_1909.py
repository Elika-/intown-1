# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150825_1909'),
        ('events', '0002_event_open_hours'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventOpenHours',
            fields=[
                ('openhours_ptr', models.OneToOneField(primary_key=True, to='core.OpenHours', auto_created=True, serialize=False, parent_link=True)),
            ],
            bases=('core.openhours',),
        ),
        migrations.AlterField(
            model_name='event',
            name='open_hours',
            field=models.ForeignKey(to='events.EventOpenHours', null=True),
        ),
        migrations.AddField(
            model_name='eventopenhours',
            name='event_fk',
            field=models.ForeignKey(to='events.Event'),
        ),
    ]
