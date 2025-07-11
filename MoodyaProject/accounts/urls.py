from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'), 
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('emotion/', views.emotion_setup, name='emotion_setup'),
    path('activity/', views.activity_level_setup, name='activity_level_setup'),
    path('region/', views.region_setup, name='region_setup'),
    path('mypage/', views.mypage, name='mypage'),   
    path('mypage/first/', views.mypage_emotion_edit, name='mypageFirst'),
    path('mypage/emotion/', views.mypage_emotion_edit, name='mypage_emotion_edit'),
    path('mypage/activity/', views.mypage_activity_edit, name='mypageSecond'),
    path('mypage/second/', views.mypage_activity_edit, name='mypage_activity_edit'),
    path('mypage/region/', views.mypage_region_edit, name='mypageThird'),
    path('mypage/region/', views.mypage_region_edit, name='mypage_region_edit'),
]