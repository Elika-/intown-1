from django.db import models
from apps.core.models import OpenHours
from django.core.validators import MinValueValidator


class Event(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=2000, blank=False, null=False)
    price = models.DecimalField(
        decimal_places=2, max_digits=5, blank=False, null=False,
        validators=[MinValueValidator(0.0)])
    event_type = models.ForeignKey('events.EventType', blank=False, null=False)
    institute = models.ForeignKey(
        'institutions.Institute', blank=False, null=False)
    address = models.ForeignKey('core.Address', null=True)

    def __str__(self):
        return self.title


class EventType(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


class EventOpenHours(OpenHours):
    event_fk = models.ForeignKey('events.Event', blank=False, null=False)
