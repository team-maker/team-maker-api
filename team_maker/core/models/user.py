from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import ugettext_lazy as _
from .player import Player


class CustomUserManager(UserManager):
    def create(self, *args, **kwargs):
        user = super(CustomUserManager, self).create(**kwargs)
        Player.objects.create(user=user)
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    photo = models.ImageField(blank=True, upload_to='uploads')

    objects = CustomUserManager()

    def __str__(self):
        return "{}".format(self.email)
