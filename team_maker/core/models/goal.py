from django.db import models


class Goal(models.Model):
    scorer = models.ForeignKey(
        'core.TeamGroupPlayer',
        null=False,
        related_name='scored_goals',
        on_delete=models.CASCADE
    )
    game = models.ForeignKey(
        'core.Game',
        null=False,
        related_name='goals',
        on_delete=models.CASCADE
    )
    own_goal = models.BooleanField(default=False)
