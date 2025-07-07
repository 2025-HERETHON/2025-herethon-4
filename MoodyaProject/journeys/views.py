from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import *


@login_required
def main(request):
    user = request.user
    profile = user.userprofile

    # 현재 열린 여정 가져오기
    journey = JourneyReview.objects.filter(
        user=user,
        is_completed=False,
        emotion=profile.emotion,
        activity_level=profile.activity_level,
        region=profile.region
    ).first()

    # 현재 여정에서 리뷰한 장소 ID만 추출
    reviewed_place_ids = []
    if journey:
        reviewed_place_ids = PlaceReview.objects.filter(journey=journey).values_list('place_id', flat=True)

    # 추천 장소 (사용자 상태에 맞고, 아직 리뷰하지 않은 곳만)
    places = (
        Place.objects
        .filter(
            emotion=profile.emotion,
            activity_level=profile.activity_level,
            region=profile.region
        )
        .exclude(id__in=reviewed_place_ids)
        .order_by('id')[:3]
    )

    # 최근 작성한 장소 리뷰 3개
    place_reviews = (
        PlaceReview.objects
        .filter(user=user)
        .select_related('place')
        .order_by('-created_at')[:3]
    )

    return render(request, 'journeys/main.html', {
        'places': places,
        'place_reviews': place_reviews
    })



@login_required
def explore(request):
    user = request.user
    profile = user.userprofile

    # 필터링된 장소들
    filtered_places = Place.objects.filter(
        emotion=profile.emotion,
        activity_level=profile.activity_level,
        region=profile.region
    )

    # 현재 열린 여정 먼저 가져오기
    journey = JourneyReview.objects.filter(
        user=user,
        is_completed=False,
        emotion=profile.emotion,
        activity_level=profile.activity_level,
        region=profile.region
    ).order_by('-created_at').first()

    # 기본값 설정
    reviewed_place_ids = []
    completed_count = 0
    total_count = filtered_places.count()

    if journey:
        reviewed_place_ids = list(
            PlaceReview.objects.filter(journey=journey).values_list('place_id', flat=True)
        )
        completed_count = len(reviewed_place_ids)

    # 기록 안 된 장소들
    unreviewed_places = filtered_places.exclude(id__in=reviewed_place_ids)

    # 기록 완료된 장소들
    reviewed_places = filtered_places.filter(id__in=reviewed_place_ids)

    # 퍼센트 계산
    progress_percent = int((completed_count / total_count) * 100) if total_count else 0

    context = {
        'unreviewed_places': unreviewed_places,
        'reviewed_places': reviewed_places,
        'completed_count': completed_count,
        'total_count': total_count,
        'progress_percent': progress_percent,
    }

    return render(request, 'journeys/explore.html', context)



@login_required
def create_place_review(request, place_id):
    user = request.user
    profile = user.userprofile
    place = get_object_or_404(Place, id=place_id)

# 감정 + 활동레벨 + 지역이 현재 상태와 일치하는 열린 여정만 가져오기
    journey = JourneyReview.objects.filter(
        user=user,
        is_completed=False,
        emotion=profile.emotion,
        activity_level=profile.activity_level,
        region=profile.region
    ).first()

# 없으면 새 여정 생성
    if not journey:
        journey = JourneyReview.objects.create(
            user=user,
            emotion=profile.emotion,
            activity_level=profile.activity_level,
            region=profile.region
        )

    if request.method == 'POST':
        rating = request.POST.get('rating')
        emotion = request.POST.get('emotion')
        comment = request.POST.get('comment')

        # 같은 여정 + 같은 장소에 이미 리뷰 쓴 적 있는지 확인
        if PlaceReview.objects.filter(user=user, place=place, journey=journey).exists():
            return redirect('journeys:explore')

        # 리뷰 생성
        PlaceReview.objects.create(
            user=user,
            place=place,
            journey=journey,
            rating=rating,
            emotion=emotion,
            comment=comment,
            created_at=timezone.now()
        )

        # 여정의 모든 장소에 리뷰가 작성되었는지 확인
        expected_places = Place.objects.filter(
            emotion=journey.emotion,
            activity_level=journey.activity_level,
            region=journey.region
        )
        reviewed_place_ids = PlaceReview.objects.filter(journey=journey).values_list('place_id', flat=True)

        if expected_places.count() == len(set(reviewed_place_ids)):
            return redirect('journeys:journey')  # 여정 정리 페이지로 이동
        return redirect('journeys:explore')  # 아직 덜 했으면 탐험 페이지로 복귀

    return render(request, 'journeys/create_place_review.html', {'place': place, 'emotion_choices': Place.EMOTION_CHOICES})


@login_required
def journey(request):
    user = request.user
    profile = user.userprofile

    # 현재 열린 여정 가져오기 (emotion + region + activity_level 일치)
    journey = JourneyReview.objects.filter(
        user=user,
        is_completed=False,
        emotion=profile.emotion,
        region=profile.region,
        activity_level=profile.activity_level
    ).first()

    # 장소 리뷰들 가져오기
    place_reviews = PlaceReview.objects.filter(journey=journey)

    if request.method == 'POST':
        content = request.POST.get('content', '')
        journey.content = content
        journey.is_completed = True
        journey.save()

        # 새로운 여정 시작
        JourneyReview.objects.create(
            user=user,
            emotion=profile.emotion,
            region=profile.region,
            activity_level=profile.activity_level
        )

        return redirect('accounts:mypage')

    return render(request, 'journeys/journey.html', {'journey': journey, 'place_reviews': place_reviews})



@login_required
def journey_detail(request, journey_id):
    journey = get_object_or_404(JourneyReview, id=journey_id, user=request.user)
    place_reviews = PlaceReview.objects.filter(journey=journey)

    return render(request, 'journeys/journey_detail.html', {
        'journey': journey,
        'place_reviews': place_reviews,
    })



@login_required
def delete_journey(request, journey_id):
    journey = get_object_or_404(JourneyReview, id=journey_id, user=request.user)
    journey.delete()
    return redirect('accounts:mypage')