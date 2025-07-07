from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('mypage/', mypage, name='mypage'),
]