from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from journeys.models import *

@login_required
def mypage(request):
    profile = request.user.userprofile
    liked_places = profile.liked_places.all()

    return render(request, 'accounts/mypage.html', {
        'liked_places': liked_places
    })