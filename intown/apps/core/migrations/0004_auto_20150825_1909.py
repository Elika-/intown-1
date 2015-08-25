# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150825_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openhours',
            name='closes_at',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='openhours',
            name='opens_at',
            field=models.TimeField(),
        ),
    ]
