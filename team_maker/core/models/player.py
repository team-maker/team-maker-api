from django.db import models
from enum import Enum


class Experience(Enum):
    AMATEUR = 'AMATEUR'
    FEDERATE = 'FEDERATE'
    SEMI_PROFESSIONAL = 'SEMI_PROFESSIONAL'
    PROFESSIONAL = 'PROFESSIONAL'


class Player(models.Model):
    user = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        related_name='players'
    )
    experience = models.CharField(
        max_length=50,
        choices=[
            (Experience.AMATEUR, ('AMATEUR')),
            (Experience.FEDERATE, ('FEDERATE')),
            (Experience.SEMI_PROFESSIONAL, ('SEMI_PROFESSIONAL')),
            (Experience.PROFESSIONAL, ('PROFESSIONAL'))
        ]
    )

    def __str__(self):
        return "{}".format(self.user)
