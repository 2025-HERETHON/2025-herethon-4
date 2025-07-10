from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone
from datetime import date

from .forms import EmotionForm, ActivityLevelForm, RegionForm
from .models import UserProfile

# 회원가입
def signup(request):
    if request.method == 'POST':
        email      = request.POST.get('email', '').strip()
        password   = request.POST.get('password', '')
        name       = request.POST.get('name', '').strip()
        is_female  = request.POST.get('is_female')

        if not is_female:
            return render(request, 'signup.html', {'error': '회원가입을 위해서는 “여성” 항목에 체크해 주세요.'})
        if not (email and password and name):
            return render(request, 'signup.html', {'error': '모든 필드를 입력해 주세요.'})
        if User.objects.filter(username=name).exists():
            return render(request, 'signup.html', {'error': '이미 사용 중인 이름입니다.'})
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': '이미 가입된 이메일입니다.'})

        user = User.objects.create_user(username=name, password=password, email=email)
        UserProfile.objects.create(user=user)
        auth_login(request, user)
        return redirect('accounts:emotion_setup')

    return render(request, 'signup.html')

# 로그인
def login(request):
    if request.method == 'POST':
        email    = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error_message': '등록되지 않은 이메일입니다.'})

        user = authenticate(request, username=user_obj.username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('accounts:emotion_setup')
        else:
            return render(request, 'login.html', {'error_message': '이메일 또는 비밀번호가 잘못되었습니다.'})

    return render(request, 'login.html')

# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect('home')

# 감정 선택
@login_required
def emotion_setup(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = EmotionForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(get_next_url(request, 'accounts:activity_level_setup'))
    else:
        form = EmotionForm(instance=profile)
    return render(request, 'accounts/emotion_setup.html', {'form': form, 'next': request.GET.get('next')})

# 활동 수준 선택
@login_required
def activity_level_setup(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ActivityLevelForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(get_next_url(request, 'accounts:region_setup'))
    else:
        form = ActivityLevelForm(instance=profile)
    return render(request, 'accounts/activity_level.html', {'form': form, 'next': request.GET.get('next')})

# 지역 선택
@login_required
def region_setup(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = RegionForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(get_next_url(request, 'home'))
    else:
        form = RegionForm(instance=profile)
    return render(request, 'accounts/region_setup.html', {'form': form, 'next': request.GET.get('next')})

# 마이페이지
@login_required
def mypage(request):
    user = request.user
    profile, _ = UserProfile.objects.get_or_create(user=user)

    today = timezone.localdate()
    joined_day = timezone.localdate(user.date_joined)
    days = (today - joined_day).days + 1

    context = {
        'days': days,
        'profile': profile,
    }
    return render(request, 'accounts/mypage.html', context)

# next URL helper
def get_next_url(request, fallback_name):
    return request.POST.get('next') or request.GET.get('next') or reverse(fallback_name)
