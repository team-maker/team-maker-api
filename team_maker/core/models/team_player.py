from django.db import models
from django.core.validators import MinValueValidator


class TeamPlayer(models.Model):
    player = models.ForeignKey(
        'core.Player',
        on_delete=models.CASCADE,
        related_name='team_players'
    )
    points_total = models.IntegerField(
        default=0,
        validators=[MinValueValidator(1)]
    )
    team = models.ForeignKey(
        'core.Team',
        on_delete=models.CASCADE,
        related_name='team_players'
    )
    admin = models.BooleanField(default=False)


    def __str__(self):
        return "{}".format('team player:' + self.player.user.email + '-' + self.team.name)
