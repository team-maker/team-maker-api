from django.db import models
from django.db.models.functions import Coalesce
from django.core.validators import MinValueValidator


class TeamGroupPlayer(models.Model):
    team_group = models.ForeignKey(
        'core.TeamGroup',
        on_delete=models.CASCADE,
        related_name='team_group_players'
    )
    team_player = models.ForeignKey(
        'core.TeamPlayer',
        on_delete=models.CASCADE,
        related_name='team_group_players'
    )
    points_amount = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0
    )

    def recalculate_points_amount(self):
        values = self.points.aggregate(
            points=Coalesce(models.Sum('points_amount'), 0)
        )
        self.points_amount = values['points']
        self.save()

    def team_goals_scored(self):
        return self.team_group.goals()


    def __str__(self):
        return "team player: {} - {}".format(self.team_player.player.user.email,  self.points_amount)
