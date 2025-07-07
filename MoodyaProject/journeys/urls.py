from django.urls import path
from .views import *

app_name = 'journeys'

urlpatterns = [
    path('', main, name='main'),
    path('explore/', explore, name='explore'),
    path('<int:place_id>/create-review/', create_place_review, name='create_place_review'),
    path('journey/', journey, name='journey'),
    path('detail/<int:journey_id>/', journey_detail, name='journey_detail'),
    path('journey/<int:journey_id>/delete/', delete_journey, name='delete_journey'),
]