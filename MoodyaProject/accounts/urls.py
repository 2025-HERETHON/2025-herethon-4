from django.urls import path
from accounts import views

app_name = "accounts"  # namespace가 accounts라는 이름을 가졌음을 명시

urlpatterns = [
    path('signup/', views.signup, name='signup'), 
    # accounts/signup/ 으로 가면 signup view를 호출
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('emotion/', views.emotion_setup, name='emotion_setup'),
    path('activity/', views.activity_level_setup, name='activity_level_setup'),
    path('region/', views.region_setup, name='region_setup'),
]