from django.shortcuts import render, redirect

from core.utils import get_traveler_profile
from traveler.forms import CreateTravelerForm, EditTravelerForm, DeleteTravelerForm
from trip.models import Trip


def create_traveler(request):
    traveler = get_traveler_profile()
    form = CreateTravelerForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('all_trips')

    context = {
        'traveler': traveler,
        'form': form,
    }

    return render(request, 'create-traveler.html', context)


def details_traveler(request):
    traveler = get_traveler_profile()
    trips_count = traveler.trips.count()

    context = {
        'traveler': traveler,
        'trips_count': trips_count,
    }

    return render(request, 'details-traveler.html', context)


def edit_traveler(request):
    traveler = get_traveler_profile()
    form = EditTravelerForm(instance=traveler)
    if request.method == 'POST':
        form = EditTravelerForm(request.POST, instance=traveler)
        if form.is_valid():
            form.save()
            return redirect('details_traveler')

    context = {
        'traveler': traveler,
        'form': form,
    }

    return render(request, 'edit-traveler.html', context)


def delete_traveler(request):
    traveler = get_traveler_profile()
    form = DeleteTravelerForm(instance=traveler)
    if request.method == 'POST':
        traveler.delete()
        return redirect('index')

    context = {
        'traveler': traveler,
        'form': form,
    }

    return render(request, 'delete-traveler.html', context)
