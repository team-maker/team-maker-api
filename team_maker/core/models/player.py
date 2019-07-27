from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Player(models.Model):
    player = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='player')
    points = models.IntegerField(default=0)
    experience = models.CharField(
        choices=[(Experience.AMATEUR, ('AMATEUR')), (Experience.FEDERATE, ('FEDERATE')),
                 (Experience.SEMI_PROFESSIONAL, ('SEMI_PROFESSIONAL')), (Experience.PROFESSIONAL, ('PROFESSIONAL'))])

    def __str__(self):
        return "{}".format(self.player)


class Experience(enu.Enum):
    AMATEUR = 'AMATEUR'
    FEDERATE = 'FEDERATE'
    SEMI_PROFESSIONAL = 'SEMI_PROFESSIONAL'
    PROFESSIONAL = 'PROFESSIONAL'
