from django.db import models
from django.conf import settings
from django.contrib.auth.models import Player, Team


class Team_Player(models.Model):
    team_player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='team_player')
    points = models.IntegerField(default=0)
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format('team_player' + self.team_player + ' ' + self.team)
