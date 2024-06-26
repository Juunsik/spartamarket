from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    follow = models.ManyToManyField(
        "self", related_name="follows", symmetrical=False
    )
    image=models.ImageField(upload_to='avatars/', default='avatars/default_avatar.png')
