from django.db import models


class TeamGroupPlayer(models.Model):
    team_group = models.ForeignKey(
        'core.TeamGroup',
        on_delete=models.CASCADE,
        related_name='team_group_players'
    )
    team_player = models.ForeignKey(
        'core.TeamPlayer',
        on_delete=models.CASCADE,
        related_name='team_group_players'
    )


    def __str__(self):
        return "{}".format('team player:' + self.player.user.email + '-' + self.team.name)
