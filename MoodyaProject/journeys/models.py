from django.db import models
from django.conf import settings

class Place(models.Model):
    EMOTION_CHOICES = [
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
    summary = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    emotion = models.CharField(max_length=20, choices=EMOTION_CHOICES)
    activity_level = models.CharField(max_length=20, choices=ACTIVITY_LEVEL_CHOICES)
    region = models.CharField(max_length=20, choices=REGION_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    tags = models.CharField(max_length=20)
    emoji = models.CharField(max_length=5)
    safety_score = models.IntegerField()
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_places', blank=True)

    def __str__(self):
        return self.name

class JourneyReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    emotion = models.CharField(max_length=20, choices=Place.EMOTION_CHOICES)
    activity_level = models.CharField(max_length=20, choices=Place.ACTIVITY_LEVEL_CHOICES)
    region = models.CharField(max_length=20, choices=Place.REGION_CHOICES)

    content = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} 여정"
    
class PlaceReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='reviews')
    journey = models.ForeignKey(JourneyReview, on_delete=models.CASCADE, related_name='reviews')

    rating = models.IntegerField()
    emotion = models.CharField(max_length=20, choices=Place.EMOTION_CHOICES)
    comment = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.place.name} ({self.rating})"
