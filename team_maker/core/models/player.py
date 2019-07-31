from django.db import models


EXPERIENCE_TYPES = (
    ('amateur', 'Amateur'),
    ('federate', 'Federate'),
    ('semi_professional', 'Semi Professional'),
    ('professional', 'Professional')
)


class Player(models.Model):
    user = models.OneToOneField(
        'core.User',
        on_delete=models.CASCADE,
        related_name='player'
    )
    experience = models.CharField(
        max_length=50,
        choices=EXPERIENCE_TYPES
    )

    def __str__(self):
        return "{}".format(self.user)
