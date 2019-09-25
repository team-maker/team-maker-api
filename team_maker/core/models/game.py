from django.db import models
from django.db.models.functions import Coalesce
from .game_available_player import GameAvailablePlayer


class CustomGameManager(models.Manager):
    def create(self, *args, **kwargs):
        game = super(CustomGameManager, self).create(*args, **kwargs)
        for team_player in game.team.team_players.all():
            GameAvailablePlayer.objects.create(
                game=game,
                team_player=team_player
            )
        return game


class Game(models.Model):
    objects = CustomGameManager()

    team = models.ForeignKey(
        'core.Team',
        null=False,
        related_name='team',
        on_delete=models.DO_NOTHING
    )
    home_team = models.OneToOneField(
        'core.TeamGroup',
        null=True,
        related_name='game_as_home_team',
        on_delete=models.CASCADE
    )
    away_team = models.OneToOneField(
        'core.TeamGroup',
        null=True,
        related_name='game_as_away_team',
        on_delete=models.CASCADE
    )
    date = models.DateField(null=True)
    finished = models.BooleanField(default=False)

    def own_goals(self):
        return self.goals.filter(own_goal=True)

    def scored_goals(self):
        return self.goals.filter(own_goal=False)

    def game_mvps(self):
        points_max = self.game_team_group_players().aggregate(
            models.Max('points_amount')
        )['points_amount__max']
        return self.game_team_group_players().filter(points_amount=points_max)

    def home_team_goals(self):
        return self.home_team.goals()

    def away_team_goals(self):
        return self.away_team.goals()

    def home_team_group_players(self):
        return self.home_team.team_group_players.all()

    def away_team_group_players(self):
        return self.away_team.team_group_players.all()

    def game_team_group_players(self):
        return (self.home_team_group_players() | self.away_team_group_players())

    def winner_team(self):
        home_team_goals = self.home_team.goals().count()
        away_team_goals = self.away_team.goals().count()
        if (home_team_goals > away_team_goals):
            return self.home_team
        elif (away_team_goals > home_team_goals):
            return self.away_team
        else:
            return None

    def home_team_clean_sheet(self):
        return self.away_team_goals().count() == 0

    def away_team_clean_sheet(self):
        return self.home_team_goals().count() == 0

    def generated_points(self):
        values = self.game_team_group_players().aggregate(
            points=Coalesce(models.Sum('points_amount'), 0)
        )
        return values['points']


    def __str__(self):
        return "Game at {} for Team: {}".format(self.date, self.team.name)