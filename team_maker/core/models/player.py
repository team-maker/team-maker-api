from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Player(models.Model):
    player = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='player')
    points = models.IntegerField(default=0)
    experience = Experience

    def __str__(self):
        return "{}".format(self.player)


class Experience(Enum):
    AMATEUR = 0
    FEDERATE = 1000
    SEMI_PROFESSIONAL = 2000
    PROFESSIONAL = 3000


# exemplo
# class Article(models.Model):
#    headline = models.CharField(max_length=100)
#    pub_date = models.DateField()
#    reporter = models.ForeignKey(
#        User, on_delete=models.CASCADE, related_name='reporter')
