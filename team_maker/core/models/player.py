from enum import Enum
from django.db import models
from django.conf import settings


class Player(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='player')
    points = models.IntegerField(default=0)
    experience = Experience


class Experience(Enum):
    AMATEUR = 0
    FEDERATE = 1000
    SEMI_PROFESSIONAL = 2000
    PROFESSIONAL = 3000
