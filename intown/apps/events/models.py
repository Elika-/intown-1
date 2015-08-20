from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=2000, blank=False, null=False)
    price = models.DecimalField(
        decimal_places=2, max_digits=5, blank=False, null=False)
    event_type = models.ForeignKey('events.EventType', blank=False, null=False)
    institute = models.ForeignKey(
        'institutions.Institute', blank=False, null=False)
    address = models.ForeignKey('core.Address', null=True)


class EventType(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
