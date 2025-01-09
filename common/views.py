from django.shortcuts import render

from core.utils import get_traveler_profile, get_all_trips


def index(request):
    return render(request, 'index.html')


def all_trips(request):
    traveler = get_traveler_profile()
    trips = get_all_trips()
    context = {
        'traveler': traveler,
        'trips': trips,
    }
    return render(request, 'all-trips.html', context)


