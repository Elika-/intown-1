from django.db import models


class Country(models.Model):
    iso3166 = models.CharField(max_length=2, blank=False, null=False)


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
