from django.core.validators import MinLengthValidator
from django.db import models

from traveler.models import Traveler


class Trip(models.Model):
    destination = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
        blank=False,
        null=False,
    )
    summary = models.TextField(
        blank=False,
        null=False,
    )
    start_date = models.DateField(
        blank=False,
        null=False,
    )
    duration = models.PositiveSmallIntegerField(
        blank=False,
        null=False,
        default=1,
        help_text="*Duration in days is expected.",
    )
    image_url = models.URLField(
        blank=True,
        null=True,
    )
    traveler = models.ForeignKey(
        Traveler,
        on_delete=models.CASCADE,
        related_name='trips',
    )

    def __str__(self):
        return self.destination

