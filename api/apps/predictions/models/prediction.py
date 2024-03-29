from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from api.apps.locations.models import Location


@python_2_unicode_compatible
class Prediction(models.Model):
    class Meta:
        app_label = 'predictions'
        unique_together = ('location', 'datetime')

    datetime = models.DateTimeField(unique=False)
    location = models.ForeignKey(Location)

    tide_level = models.FloatField(
        help_text='The predicted height in metres of the tidal component '
                  'of the sea level above a known datum.')

    def __str__(self):
        return "{} @ {}".format(self.datetime, self.location.name)
