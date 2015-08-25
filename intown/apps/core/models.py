from django.db import models


class Country(models.Model):
    iso3166 = models.CharField(max_length=2, blank=False, null=False)

    def __str__(self):
        return self.iso3166


class Address(models.Model):
    address_line_1 = models.CharField(max_length=100, blank=False, null=False)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=False, null=False)
    city = models.CharField(max_length=60, blank=False, null=False)
    state = models.CharField(max_length=60)
    country = models.ForeignKey('core.Country', blank=False, null=False)

    lat = models.DecimalField(
        blank=True, null=True, decimal_places=4, max_digits=7)
    lng = models.DecimalField(
        blank=True, null=True, decimal_places=4, max_digits=7)

    phone = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.address_line_1 + self.zip_code + self.city


class OpenHours(models.Model):
    DAY_CHOICES = (
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday')
    )

    day_of_week = models.CharField(
        choices=DAY_CHOICES, max_length=3, blank=False, null=False)
    opens_at = models.TimeField()
    closes_at = models.TimeField()

    def __str__(self):
        return self.day_of_week
