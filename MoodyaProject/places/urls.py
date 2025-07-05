# places/urls.py
from django.urls import path
from .views import *

app_name = 'places'

urlpatterns = [
    path('list/', place_list, name='place_list'),
]
