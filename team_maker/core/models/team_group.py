from django.db import models
from django.core.validators import MinValueValidator
from .goal import Goal


class TeamGroup(models.Model):
    team = models.ForeignKey(
        'core.Team',
        on_delete=models.CASCADE,
        related_name='team_groups'
    )
    game = models.ForeignKey(
        'core.Game',
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
        return Goal.objects.filter(scorer__id__in=team_group_ids).all()

    def mvps(self):
        self.team_group_players.order_by('-points_amount')

    def hattricks(self):
        scorer_ids = self.goals() \
            .filter(own_goal=False) \
            .values('scorer') \
            .annotate(total=models.Count('scorer')) \
            .filter(total__gte=3) \
            .values('scorer')
        return self.team_group_players.filter(pk__in=scorer_ids)


    def __str__(self):
        return "Group of team {} with: {} players".format(self.team.name, self.number_of_players)
