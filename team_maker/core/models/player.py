from django.db import models
from enum import Enum
from django.conf import settings
from .user import User


class Experience(Enum):
    AMATEUR = 'AMATEUR'
    FEDERATE = 'FEDERATE'
    SEMI_PROFESSIONAL = 'SEMI_PROFESSIONAL'
    PROFESSIONAL = 'PROFESSIONAL'


class Player(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    points = models.IntegerField(default=0)
    experience = models.CharField(
        choices=[(Experience.AMATEUR, ('AMATEUR')), (Experience.FEDERATE, ('FEDERATE')),
                 (Experience.SEMI_PROFESSIONAL, ('SEMI_PROFESSIONAL')), (Experience.PROFESSIONAL, ('PROFESSIONAL'))])

    def __str__(self):
        return "{}".format(self.player)
