from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_author = models.BooleanField(default=False)
    profile = models.ImageField(default='defaults/user_default.jpg', upload_to='user/')

    def __str__(self):
        return self.username