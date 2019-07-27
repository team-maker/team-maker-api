from django.db import models
from django.conf import settings
from .player import Player
from .team import Team


class Team_Player(models.Model):
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='player')
    points = models.IntegerField(default=0)
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format('team player:' + self.team_player + ' ' + self.team)
