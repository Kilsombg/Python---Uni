from django.shortcuts import render, redirect
from .models import Information

# Create your views here.
full_stars = 0
half_stars = 0
empty_stars = 10
rating = 0


def index(request):
    info = Information.objects.get(id=1)
    context = {
        'full_stars': range(full_stars),
        'half_stars': range(half_stars),
        'empty_stars': range(empty_stars),
        'rating': rating,
        'info': info,
    }
    return render(request, 'rating_app/index.html', context)


def draw_rating(request):
    global rating
    rating = int(request.GET['rating'])
    info = Information.objects.get(id=1)
    info.rating = rating
    info.save()

    return calc_rating()


def calc_rating():
    global rating, full_stars, half_stars, empty_stars
    full_stars = rating * 10 // 100
    empty_stars = (100-rating) * 10 // 100
    half_stars = 10 - full_stars - empty_stars
    return redirect('/')
