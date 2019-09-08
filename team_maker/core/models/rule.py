from django.db import models

RULE_TYPES = (
    ('presence', 'Presence'),
    ('goal', 'Goal'),
    ('hattrick', 'Hattrick'),
    ('goals_conceded', 'Goals Conceded'),
    ('goals_scored', 'Goal Scored'),
    ('clean_sheet', 'Clean Sheet'),
    ('own_goal', 'Own Goal'),
    ('game_victory', 'Game Victory'),
    ('game_defeat', 'Game Defeat'),
    ('game_mvp', 'Game MVP'),
)


class Rule(models.Model):
    description = models.CharField(
        max_length=80,
        unique=True
    )
    rule_type = models.CharField(
        max_length=50,
        choices=RULE_TYPES,
        unique=True
    )
    default_points = models.IntegerField(
        default=1
    )
