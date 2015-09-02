# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_remove_event_open_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.DecimalField(max_digits=5, validators=[django.core.validators.MinValueValidator(0.0)], decimal_places=2),
        ),
    ]
