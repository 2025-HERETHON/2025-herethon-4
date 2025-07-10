from django.contrib import admin
<<<<<<< HEAD
from .models import *
=======
from .models import UserProfile
>>>>>>> 김민기

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'emotion', 'activity_level', 'region')
    search_fields = ('user__username', 'user__email')
    list_filter = ('emotion', 'activity_level', 'region')