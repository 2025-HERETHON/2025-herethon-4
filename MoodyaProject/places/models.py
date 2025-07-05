from django.db import models
from django.contrib.auth.models import User

class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    mood_tag = models.CharField(max_length=20)
    activity_tag = models.CharField(max_length=20)
    region_tag = models.CharField(max_length=20)

    def __str__(self):
        return self.name
