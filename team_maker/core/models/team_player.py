from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.functions import Coalesce
from .point import Point
from .game import Game
from .goal import Goal


class TeamPlayer(models.Model):
    player = models.ForeignKey(
        'core.Player',
        on_delete=models.CASCADE,
        related_name='team_players'
    )
    points_total = models.IntegerField(
        default=0,
        validators=[MinValueValidator(1)]
    )
    position = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )
    team = models.ForeignKey(
        'core.Team',
        on_delete=models.CASCADE,
        related_name='team_players'
    )
    admin = models.BooleanField(default=False)

    def points(self):
        return Point.objects.filter(team_group_player__team_player_id=self.id)

    def games_played(self):
        game_ids = self.team_group_players.values_list('team_group__game_id', flat=True)
        return Game.objects.filter(pk__in=game_ids, finished=True)

    def goals_scored(self):
        team_group_player_ids = self.team_group_players.values_list('pk', flat=True)
        return Goal.objects.filter(scorer_id__in=team_group_player_ids, own_goal=False)

    def own_goals(self):
        team_group_player_ids = self.team_group_players.values_list('pk', flat=True)
        return Goal.objects.filter(scorer_id__in=team_group_player_ids, own_goal=True)

    def recalculate_points_amount(self):
        values = self.team_group_players.aggregate(
            points=Coalesce(models.Sum('points_amount'), 0)
        )
        self.points_total = values['points']
        self.save()


    def __str__(self):
        return "{}".format('team player:' + self.player.user.email + '-' + self.team.name)
