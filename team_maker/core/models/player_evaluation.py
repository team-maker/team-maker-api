from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class PlayerEvaluation(models.Model):
    evaluated_player = models.ForeignKey(
        'core.TeamPlayer',
        null=False,
        related_name='other_evaluations',
        on_delete=models.CASCADE
    )
    evaluator_player = models.ForeignKey(
        'core.TeamPlayer',
        null=False,
        related_name='performed_evaluations',
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    def clean(self):
        # Team Players should belong to the same team.
        if self.evaluated_player.team != self.evaluator_player.team:
            raise ValidationError(_('Players should belong to the same team'))
