import string
from django.core.exceptions import ValidationError


def is_valid_fio(value):
    if len(value.split()) == 3:
        for word in value.split():
            for letter in word:
                if letter not in string.ascii_letters:
                    raise ValidationError('Only letters')
        return value
    else:
        raise ValidationError('Enter first second and last name')