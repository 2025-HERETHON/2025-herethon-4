from django.urls import path
from .views import *

app_name = 'places'

urlpatterns = [
    path('', main, name='main'),
    path('recommend-places/', recommend_places, name='recommend_places'),
    path('detail-place/<int:id>/', detail_place, name='detail_place'),
    path('create-review/<int:id>/', create_review, name="create_review"),
    path('update-review/<int:id>/', update_review, name="update_review"),
    path('delete-review/<int:id>/', delete_review, name="delete_review"),
]