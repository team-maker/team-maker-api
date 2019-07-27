from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    photo = models.ImageField(upload_to='uploads', blank=True)
    players = models.ManyToManyField(Player, through='Player')

    def __str__(self):
        return "{}".format(self.email)
