from django.shortcuts import render
from .models import Place

def place_list(request):
    # 데모용 하드코딩
    mood = "활기차요"
    activity_level = "초급"
    region = "서북권"

    places = Place.objects.filter(
        mood_tag=mood,
        activity_tag=activity_level,
        region_tag=region
    )

    return render(request, 'places/place_list.html', {'places': places})