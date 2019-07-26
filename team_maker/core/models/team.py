from django.db import models
from django.conf import settings
from django.contrib.auth.models import Player


class Team(models.Model):
    name = models.CharField(max_length=130)
    admin = models.OneToOneField(
        Player, on_delete=models.CASCADE, primary_key=True,)

    def __str__(self):
        return "{}".format(self.name)
