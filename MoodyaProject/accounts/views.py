from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
import uuid  
from datetime import date
from django.contrib.auth.decorators import login_required
from .forms import EmotionForm
from .forms import ActivityLevelForm
from .forms import RegionForm
from .models import UserProfile
from accounts.models import UserProfile
from django.urls import reverse 
from django.utils import timezone
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        email      = request.POST.get('email', '').strip()
        password   = request.POST.get('password', '')
        name       = request.POST.get('name', '').strip()   # 사용자 입력 이름
        is_female  = request.POST.get('is_female')          # 체크박스, 미선택 시 None

        # --- 유효성 검사 ---
        if not is_female:
            return render(request, 'signup.html', {
                'error': '회원가입을 위해서는 “여성” 항목에 체크해 주세요.'
            })

        if not (email and password and name):
            return render(request, 'signup.html', {
                'error': '모든 필드를 입력해 주세요.'
            })

        if User.objects.filter(username=name).exists():
            return render(request, 'signup.html', {
                'error': '이미 사용 중인 이름입니다.'
            })

        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {
                'error': '이미 가입된 이메일입니다.'
            })

        # --- 사용자 생성 ---
        user = User.objects.create_user(
            username=name,   # 이름을 username으로 저장
            password=password,
            email=email
        )

        # --- UserProfile 직접 생성 ---
        UserProfile.objects.create(user=user)

        # --- 자동 로그인 후 감정 선택 화면으로 이동 ---
        auth_login(request, user)
        return redirect('accounts:emotion_setup')

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email    = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        # 1) 이메일로 사용자 조회
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'login.html', {
                'error_message': '등록되지 않은 이메일입니다.'
            })

        # 2) 찾은 사용자의 username을 이용해 인증
        user = authenticate(request,
                            username=user_obj.username,
                            password=password)

        if user is not None:
            auth_login(request, user)
            print('로그인 성공:', user.username)
            return redirect('accounts:emotion_setup')
        else:
            return render(request, 'login.html', {
                'error_message': '이메일 또는 비밀번호가 잘못되었습니다.'
            })

    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    print('로그아웃 성공')
    return redirect('home')


@login_required
def emotion_setup(request):
    # 프로필이 없으면 새로 만듦 → 에러 방지용 안전 코드
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = EmotionForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:activity_level_setup')
    else:
        form = EmotionForm(instance=profile)

    return render(request, 'accounts/emotion_setup.html', {'form': form})

@login_required
def activity_level_setup(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ActivityLevelForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:region_setup')
    else:
        form = ActivityLevelForm(instance=profile)

    return render(request, 'accounts/activity_level.html', {'form': form})

@login_required
def region_setup(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = RegionForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = RegionForm(instance=profile)

    return render(request, 'accounts/region_setup.html', {'form': form})

def get_next_url(request, fallback_name):
    return request.POST.get('next') or request.GET.get('next') or reverse(fallback_name)

# ────────────── 마이페이지 ──────────────
@login_required
def mypage(request):
    user = request.user
    profile, _ = UserProfile.objects.get_or_create(user=user)

    today       = timezone.localdate()                  
    joined_day  = timezone.localdate(user.date_joined) 
    days        = (today - joined_day).days + 1        

    context = {
        'days': days,
        'profile': profile,
    }
    return render(request, 'accounts/mypage.html', context)

# ───── 감정 선택 ─────
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

    return render(request, 'accounts/emotion_setup.html', {
        'form': form,
        'next': request.GET.get('next')
    })

# ───── 활동 수준 선택 ─────
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

    return render(request, 'accounts/activity_level.html', {
        'form': form,
        'next': request.GET.get('next')
    })

# ───── 지역 선택 ─────
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

    return render(request, 'accounts/region_setup.html', {
        'form': form,
        'next': request.GET.get('next')
    })
