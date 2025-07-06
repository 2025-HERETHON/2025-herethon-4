from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from places.models import *

def mypage(request):
    return render(request, 'accounts/mypage.html')

@login_required
def visits(request):
    reviews = Review.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'accounts/visits.html', {'reviews': reviews})