from django.db import models
from django.conf import settings
from django.contrib.auth.models import Player
from django.utils.crypto import get_random_string


class Team(models.Model):
    name = models.CharField(max_length=130)
    players = models.ManyToManyField(Player, through='Team_Player')
    token = get_random_string(length=10)

    def __str__(self):
        return "{}".format(self.name)
