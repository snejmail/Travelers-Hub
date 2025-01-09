from django.core.exceptions import ValidationError


def validate_letters_digits_string(value):
    if not value.isalnum():
        raise ValidationError('Your nickname is invalid!')

