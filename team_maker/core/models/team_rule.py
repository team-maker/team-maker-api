from django.db import models
from django.core.validators import MinValueValidator


class TeamRule(models.Model):
    rule = models.ForeignKey(
        'core.Rule',
        on_delete=models.CASCADE,
        related_name='team_rules'
    )
    team = models.ForeignKey(
        'core.Team',
        on_delete=models.CASCADE,
        related_name='team_rules'
    )
    points_amount = models.IntegerField(
        validators=[MinValueValidator(1)]
    )
