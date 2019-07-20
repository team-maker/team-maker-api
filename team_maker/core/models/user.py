from enum import Enum
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


def __str__(self):
    return "{}".format(self.email)


class UserPlayer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    points = models.IntegerField(default=0)
    exp = Experiencia
    photo = models.ImageField(upload_to='uploads', blank=True)


class Experiencia(Enum):
    AMADOR = 0
    FEDERADO = 1000
    SEMI_PROFISSIONAL = 2000
    PROFISSIONAL = 3000
