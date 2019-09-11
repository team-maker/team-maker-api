from django.db import models

AVAILABLE_TYPES = (
    ('unknown', 'Unknown'),
    ('going', 'Going'),
    ('not_going', 'Not Going'),
)


class GameAvailablePlayer(models.Model):
    team_player = models.ForeignKey(
        'core.TeamPlayer',
        on_delete=models.CASCADE,
        related_name='available_players'
    )
    game = models.ForeignKey(
        'core.Game',
        on_delete=models.CASCADE,
        related_name='available_players'
    )
    availability = models.CharField(
        max_length=50,
        choices=AVAILABLE_TYPES,
        default='unknown'
    )

    def __str__(self):
        return "Team Player: {} - {}".format(self.team_player + '-' + self.availability)
