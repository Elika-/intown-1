# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150825_1909'),
        ('institutions', '0004_auto_20150825_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstituteAddress',
            fields=[
                ('address_ptr', models.OneToOneField(primary_key=True, to='core.Address', parent_link=True, auto_created=True, serialize=False)),
            ],
            bases=('core.address',),
        ),
        migrations.RemoveField(
            model_name='institute',
            name='address',
        ),
        migrations.AddField(
            model_name='instituteaddress',
            name='institute_fk',
            field=models.ForeignKey(to='institutions.Institute'),
        ),
    ]
