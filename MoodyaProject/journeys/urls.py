from django.urls import path
from .views import *

app_name = 'journeys'

urlpatterns = [
    path('', main, name='main'),
    path('explore/', explore, name='explore'),
    path('create-review/<int:place_id>/', create_place_review, name='create_place_review'),
    path('journey/', journey, name='journey'),
    path('jouney/like/<int:place_id>', like_place, name='like_place'),
]