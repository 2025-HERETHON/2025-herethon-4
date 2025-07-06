from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
import uuid  
from django.contrib.auth.decorators import login_required
from .forms import EmotionForm
from .forms import ActivityLevelForm
from .forms import RegionForm
from .models import UserProfile
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

        print('회원가입 성공:', user.username)
        return redirect('home')

    # GET 요청
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

    # GET 요청
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