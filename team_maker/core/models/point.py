from django.db import models
from django.core.validators import MinValueValidator


class Point(models.Model):
    team_group_player = models.ForeignKey(
        'core.TeamGroupPlayer',
        null=False,
        related_name='points',
        on_delete=models.CASCADE
    )
    team_rule = models.ForeignKey(
        'core.TeamRule',
        null=False,
        related_name='points',
        on_delete=models.CASCADE
    )
    description = models.CharField(
        max_length=80
    )
    points_amount = models.IntegerField(
        validators=[MinValueValidator(1)]
    )

    def __str__(self):
        return "{}".format('team group player:' + self.team_group_player + '-' + self.points_amount)