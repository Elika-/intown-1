# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(null=True, blank=True, max_length=500)),
                ('address_line_1', models.CharField(max_length=100)),
                ('address_line_2', models.CharField(null=True, blank=True, max_length=100)),
                ('zip_code', models.CharField(null=True, blank=True, max_length=20)),
                ('city', models.CharField(null=True, blank=True, max_length=60)),
                ('state', models.CharField(max_length=60)),
                ('website', models.URLField()),
                ('country', models.ForeignKey(to='core.Country')),
            ],
        ),
        migrations.CreateModel(
            name='OpenHours',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('day_of_week', models.CharField(choices=[('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THU', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday'), ('SUN', 'Sunday')], max_length=3)),
                ('opens_at', models.PositiveSmallIntegerField()),
                ('closes_at', models.PositiveSmallIntegerField()),
                ('institute', models.ForeignKey(to='institutions.Institute')),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('media', models.CharField(choices=[('FB', 'Facebook'), ('TW', 'Twitter'), ('IG', 'Instagram'), ('PT', 'Pinterest'), ('TM', 'Tumblr')], max_length=2)),
                ('url', models.URLField()),
                ('institute', models.ForeignKey(to='institutions.Institute')),
            ],
        ),
    ]
