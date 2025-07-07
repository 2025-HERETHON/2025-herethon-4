from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import *
from journeys.models import *

@login_required
def mypage(request):
    user = request.user

    # 완료된 여정만 가져오기
    completed_journeys = JourneyReview.objects.filter(user=user, is_completed=True).order_by('-created_at')

    return render(request, 'accounts/mypage.html', {
        'completed_journeys': completed_journeys,
    })