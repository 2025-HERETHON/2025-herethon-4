from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    EMOTION_CHOICES = [
        ('ANXIOUS',   '불안해요'),
        ('EXCITED',   '설레요'),
        ('ENERGETIC', '활기차요'),
        ('CURIOUS',   '궁금해요'),
        ('CALM',      '평온해요'),
    ]

    ACTIVITY_LEVEL_CHOICES = [
        ('BEGINNER',     '초급'),
        ('INTERMEDIATE', '중급'),
        ('ADVANCED',     '상급'),
    ]

    REGION_CHOICES = [
        ('NW', '서북권'),
        ('NE', '동북권'),
        ('SW', '서남권'),
        ('SE', '동남권'),
        ('C',  '중부권'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emotion = models.CharField(
        max_length=10,
        choices=EMOTION_CHOICES,
        null=True,
        blank=False
    )
    activity_level = models.CharField(
        max_length=12,
        choices=ACTIVITY_LEVEL_CHOICES,
        null=True,
        blank=False
    )
    region = models.CharField(
        max_length=2,
        choices=REGION_CHOICES,
        null=True,
        blank=False
    )

    def __str__(self):
        return f"{self.user.username} profile"
