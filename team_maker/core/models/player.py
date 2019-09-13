from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Player(models.Model):
    user = models.OneToOneField(
        'core.User',
        on_delete=models.CASCADE,
        related_name='player'
    )
    rating = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    def __str__(self):
        return "{} - {}".format(self.user, self.rating)
