from django.db import models
from django.contrib.auth.models import AbstractUser, Player
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    players = models.ManyToManyField(Player, through='Player')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    photo = models.ImageField(upload_to='uploads', blank=True)

    def __str__(self):
        return "{}".format(self.email)
