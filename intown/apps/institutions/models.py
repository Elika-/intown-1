from django.db import models


class Institute(models.Model):
	name = models.CharField(max_length=200, blank=False, null=False)
	description = models.CharField(max_length=500, blank=True, null=True)

	address_line_1 = models.CharField(max_length=100, blank=False, null=False)
	address_line_2 = models.CharField(max_length=100, blank=True, null=True)
	zip_code = models.CharField(max_length=20, blank=True, null=True)
	city = models.CharField(max_length=60, blank=True, null=True)
	state = models.CharField(max_length=60)
	country = models.ForeignKey('core.Country', blank=False, null=False)

	website = models.URLField()


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

	institute = models.ForeignKey('institutions.Institute', blank=False, null=False)
	day_of_week = models.CharField(choices=DAY_CHOICES, max_length=3, blank=False, null=False)
	opens_at = models.PositiveSmallIntegerField(blank=False, null=False)
	closes_at = models.PositiveSmallIntegerField(blank=False, null=False)


class SocialMedia(models.Model):
	MEDIA_CHOICES = (
		('FB', 'Facebook'),
		('TW', 'Twitter'),
		('IG', 'Instagram'),
		('PT', 'Pinterest'),
		('TM', 'Tumblr')
	)

	institute = models.ForeignKey('institutions.Institute', blank=False, null=False)
	media = models.CharField(choices=MEDIA_CHOICES, max_length=2, blank=False, null=False)
	url = models.URLField(blank=False, null=False)
