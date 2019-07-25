from django.db import models
from django.conf import settings


class Team(models.Model):
    name = models.CharField(max_length=130)
    users = []

    def __str__(self):
        return "{}".format(self.name)
