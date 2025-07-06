from django.db import models
from django.conf import settings
import os
from uuid import uuid4
from django.utils import timezone

def upload_filepath(instance, filename):
    today_str = timezone.now().strftime("%Y%m%d")
    file_basename = os.path.basename(filename)
    return f'{instance._meta.model_name}/{today_str}/{str(uuid4())}_{file_basename}'


class Place(models.Model):
    MOOD_CHOICES = [
        ('ANXIOUS', '불안해요'),
        ('EXCITED', '설레요'),
        ('ENERGETIC', '활기차요'),
        ('CURIOUS', '궁금해요'),
        ('CALM', '평온해요'),
    ]

    ACTIVITY_LEVEL_CHOICES = [
        ('BEGINNER', '초급'),
        ('INTERMEDIATE', '중급'),
        ('ADVANCED', '상급'),
    ]

    REGION_CHOICES = [
        ('NW', '서북권'),
        ('NE', '동북권'),
        ('SW', '서남권'),
        ('SE', '동남권'),
        ('C', '중부권'),
    ]

    CATEGORY_CHOICES = [
        ('자연', '자연'),
        ('카페', '카페'),
        ('전시', '전시'),
        ('책방', '책방'),
    ]

    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    address = models.CharField(max_length=200)

    emotion = models.CharField(max_length=20, choices=MOOD_CHOICES)
    activity_level = models.CharField(max_length=20, choices=ACTIVITY_LEVEL_CHOICES)
    region = models.CharField(max_length=20, choices=REGION_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    tags = models.CharField(max_length=20, null=True, blank=True)
    emoji = models.CharField(max_length=5, blank=True)
    safety_score = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_filepath, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    image = models.ImageField(upload_to=upload_filepath, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.get_username()} - {self.place.name} ({self.rating})"
