from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_female = models.BooleanField(default=False)
    name = models.CharField(max_length=20)
    mood = models.CharField(max_length=20)
    activity = models.CharField(max_length=20)
    region = models.CharField(max_length=20)

    def __str__(self):
        return self.name
