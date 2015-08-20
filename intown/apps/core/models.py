from django.db import models


class Country(models.Model):
	iso3166 = models.CharField(max_length=2, blank=False, null=False)
