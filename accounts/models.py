from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import User #1
from django.conf import settings
User = settings.AUTH_USER_MODEL

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username


