from enum import Enum

from django.core.exceptions import ValidationError
from django.utils import timezone


class ScoreChoice(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


def validate_year(value):
    if value > timezone.datetime.now().year:
        raise ValidationError('Это произведение будущего =)')
