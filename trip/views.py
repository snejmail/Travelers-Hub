from django.shortcuts import render, redirect, get_object_or_404

from core.utils import get_traveler_profile
from trip.forms import CreateTripForm, DeleteTripForm
from trip.models import Trip


def create_trip(request):
    traveler = get_traveler_profile()
    form = CreateTripForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.traveler = traveler
            form.save()
            return redirect('all_trips')

    context = {
        'traveler': traveler,
        'form': form,
    }

    return render(request, 'create-trip.html', context)


def details_trip(request, trip_id):
    trip = Trip.objects.get(pk=trip_id)
    traveler = get_traveler_profile()

    context = {
        'trip': trip,
        'traveler': traveler,
    }

    return render(request, 'details-trip.html', context)


def edit_trip(request, trip_id):
    trip = Trip.objects.get(pk=trip_id)

    if request.method == 'POST':
        form = CreateTripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('all_trips')

    else:
        form = CreateTripForm(instance=trip)

    context = {
        'trip': trip,
        'form': form,
    }

    return render(request, 'edit-trip.html', context)


def delete_trip(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)

    form = DeleteTripForm(instance=trip)
    if request.method == 'POST':
        trip.delete()
        return redirect('all_trips')

    context = {
        'trip': trip,
        'form': form,
    }

    return render(request, 'delete-trip.html', context)

