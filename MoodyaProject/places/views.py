from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .models import *

@login_required
def main(request):
    user = request.user
    profile = user.profile

    places = (
        Place.objects
        .filter(
            mood=profile.mood,
            activity=profile.activity,
            region=profile.region
        )
        .annotate(avg_rating=Avg('reviews__rating'))
        .order_by('-avg_rating')[:5]
    )

    reviews = (
        Review.objects
        .filter(user=user)
        .select_related('place')
        .order_by('-created_at')[:5]
    )

    return render(request, 'places/main.html', {'places': places, 'reviews': reviews})


@login_required
def recommend_places(request):
    user = request.user
    profile = user.profile
    category = request.GET.get('category')

    recommended_places = (
        Place.objects
        .filter(
            mood=profile.mood,
            activity=profile.activity,
            region=profile.region
        )
    )
    if category and category != "전체":
        recommended_places = recommended_places.filter(category=category)

    recommended_places = recommended_places.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')

    return render(request, 'places/recommend_places.html', {
        'recommended_places': recommended_places,
        'selected_category': category or '전체'
    })


@login_required
def detail_place(request, id):
    place = get_object_or_404(Place, id=id)
    reviews = Review.objects.filter(place=place).order_by('-created_at')

    return render(request, 'places/detail_place.html', {'place': place, 'reviews': reviews})


@login_required
def create_review(request, id):
    place = get_object_or_404(Place,id=id)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        Review.objects.create(
            user=request.user,
            place=place,
            rating=rating,
            comment=comment
        )

        return redirect('places:detail_place', id=id)
    return render(request, 'places/create_review.html', {'place':place})

@login_required
def update_review(request, id):
    review = get_object_or_404(Review, id=id, user=request.user)

    if request.method == 'POST':
        review.rating = request.POST.get('rating')
        review.comment = request.POST.get('comment')
        review.save()
        return redirect('places:detail_place', review.place.id)
    
    return render(request, 'places/update_review.html', {'review': review})

@login_required
def delete_review(request, id):
    review = get_object_or_404(Review, id=id, user=request.user)
    review.delete()
    return redirect('places:detail_place', review.place.id)