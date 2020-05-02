from django.db import models
from django.contrib.auth.models import AbstractUser
from video_api.models import Video
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    """
    Custom User model
    """
    phone = models.CharField(verbose_name='phone', unique=True, max_length=11, blank=True)
    email = models.EmailField(verbose_name='email', unique=True)
    videos = models.ManyToManyField(Video, blank=True)
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def creat_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
