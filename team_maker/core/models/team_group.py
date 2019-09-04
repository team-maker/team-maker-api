from django.db import models
from django.core.validators import MinValueValidator
from .goal import Goal


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

    def goals(self):
        team_group_ids = self.team_group_players.values_list('pk', flat=True)
        return Goal.objects.filter(team_group_id__in=team_group_ids)


    def __str__(self):
        return "Group of team {} with: {} players".format(self.team.name, self.number_of_players)
