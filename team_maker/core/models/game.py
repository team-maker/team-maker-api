from django.db import models


class Game(models.Model):
    team = models.ForeignKey(
        'core.Team',
        null=False,
        related_name='team',
        on_delete=models.CASCADE
    )
    home_team = models.ForeignKey(
        'core.TeamGroup',
        null=True,
        related_name='home_team',
        on_delete=models.CASCADE
    )
    away_team = models.ForeignKey(
        'core.TeamGroup',
        null=True,
        related_name='away_team',
        on_delete=models.CASCADE
    )
    winner_team = models.ForeignKey(
        'core.TeamGroup',
        null=True,
        related_name='winner_team',
        on_delete=models.CASCADE
    )
    date = models.DateField(null=True)

    def __str__(self):
        return "Game at {} for Team: {}".format(self.date, self.team.name)