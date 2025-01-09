from django.core.validators import MinLengthValidator
from django.db import models

from core.custom_validators import validate_letters_digits_string


class Traveler(models.Model):
    nickname = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(3),
                    validate_letters_digits_string],
        blank=False,
        null=False,
        unique=True,
        help_text="*Nicknames can contain only letters and digits."
    )
    email = models.EmailField(
        max_length=30,
        blank=False,
        null=False,
        unique=True,
    )
    country = models.CharField(
        max_length=3,
        blank=False,
        null=False,
        validators=[MinLengthValidator(3),],
    )
    about_me = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.nickname

