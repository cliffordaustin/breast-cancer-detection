from django.db import models
from django.conf import settings


class Predictions(models.Model):
    result = models.FloatField(
        null=True,
        blank=True,
    )
    first_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    age = models.IntegerField(
        null=True,
        blank=True,
    )
    location = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
