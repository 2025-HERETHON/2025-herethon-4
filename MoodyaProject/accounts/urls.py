from django.urls import path
<<<<<<< HEAD
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('mypage/', mypage, name='mypage'),
=======
from accounts import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name='signup'), 
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('emotion/', views.emotion_setup, name='emotion_setup'),
    path('activity/', views.activity_level_setup, name='activity_level_setup'),
    path('region/', views.region_setup, name='region_setup'),
    path('mypage/', views.mypage, name='mypage'),   
>>>>>>> 김민기
]