from django.db import models
from django.utils.crypto import get_random_string
from django.conf import settings
from .player import Player


class Team(models.Model):
    name = models.CharField(max_length=130)
    players = models.ManyToManyField(Player, through='Team_Player')
    token = get_random_string(length=10)

    def __str__(self):
        return "{}".format(self.name)
