from django.db import models
from apps.core.models import OpenHours


class Institute(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=500, blank=True, null=True)
    website = models.URLField()
    address = models.ForeignKey('core.Address', blank=False, null=True)

    def __str__(self):
        return self.name


class InstituteOpenHours(OpenHours):
    institute_fk = models.ForeignKey(
        'institutions.Institute', null=False, blank=False)


class SocialMedia(models.Model):
    MEDIA_CHOICES = (
        ('FB', 'Facebook'),
        ('TW', 'Twitter'),
        ('IG', 'Instagram'),
        ('PT', 'Pinterest'),
        ('TM', 'Tumblr')
    )

    institute = models.ForeignKey(
        'institutions.Institute', blank=False, null=False)
    media = models.CharField(
        choices=MEDIA_CHOICES, max_length=2, blank=False, null=False)
    url = models.URLField(blank=False, null=False)
