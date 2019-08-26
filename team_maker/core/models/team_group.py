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
    calculated_ponderation = models.FloatField(null=True)


    def __str__(self):
        return "Group of team {} with: {} players".format(self.team.name, self.number_of_players)
