from django.db import models
from django.core.validators import MinValueValidator


class TeamGroup(models.Model):
    team = models.ForeignKey(
        'core.Team',
        on_delete=models.CASCADE,
        related_name='team_groups'
    )
    number_of_players = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1)]
    )
    team_players = models.ManyToManyField(
        'core.TeamPlayer',
        through='TeamGroupPlayer',
    )


    def __str__(self):
        return "{}".format('team player:' + self.player.user.email + '-' + self.team.name)
