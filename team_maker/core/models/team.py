from django.db import models
from django.utils.crypto import get_random_string
from .rule import Rule


class TeamManager(models.Manager):
    def create(self, *args, **kwargs):
        team = super(TeamManager, self).create(*args, **kwargs)
        if not team.token:
            team.token = get_random_string()
            team.save()
        rules = Rule.objects.all()
        for rule in rules:
            team.team_rules.create(
                rule=rule,
                points_amount=rule.default_points
            )
        return team


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
    )
    photo = models.ImageField(blank=True, upload_to='uploads')

    objects = TeamManager()

    def __str__(self):
        return "{}".format(self.name)
