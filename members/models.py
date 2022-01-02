from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class EntranceKey(models.Model):
    code = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.code


class Member(AbstractUser):
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    youtube = models.CharField(max_length=50, blank=False, null=False)
    twitch = models.CharField(max_length=50, blank=False, null=False)
    twitter = models.CharField(max_length=50, blank=True, null=True)
    discord = models.CharField(max_length=50, blank=True, null=True)
    # Just in case Tencent takes over
    trobo = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.id}:{self.username}"

    # def natural_key(self):
    #     return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)