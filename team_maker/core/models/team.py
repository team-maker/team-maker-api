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
    )
    photo = models.ImageField(blank=True, upload_to='uploads')

    def __str__(self):
        return "{}".format(self.name)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = get_random_string()
        super(Team, self).save(*args, **kwargs)
