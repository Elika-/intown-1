# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20150825_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='open_hours',
        ),
    ]
