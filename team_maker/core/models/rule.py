from django.db import models
from django.core.validators import MinValueValidator

RULE_TYPES = (
    ('presence', 'Presence'),
    ('goal', 'Goal'),
    ('hattrick', 'Hattrick'),
    ('goal_conceded', 'Goal Conceded'),
    ('clean_sheet', 'Clean Sheet'),
    ('own_goal', 'Own Goal')
)


class Rule(models.Model):
    description = models.CharField(
        max_length=80,
        unique=True
    )
    rule_type = models.CharField(
        max_length=50,
        choices=RULE_TYPES
    )
    default_points = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )
