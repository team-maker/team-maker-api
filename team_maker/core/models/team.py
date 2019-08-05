from django.db import models
from django.utils.crypto import get_random_string


class Team(models.Model):
    name = models.CharField(
        max_length=40,
        unique=True
    )
    players = models.ManyToManyField(
        'core.Player',
        through='TeamPlayer',
    )
    token = models.CharField(
        max_length=40,
        unique=True,
        default=get_random_string(length=15),
    )

    def __str__(self):
        return "{}".format(self.name)
