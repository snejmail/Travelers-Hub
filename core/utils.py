from traveler.models import Traveler
from trip.models import Trip


def get_traveler_profile():
    return Traveler.objects.first()


def get_all_trips():
    return Trip.objects.all().order_by('-start_date') if Trip.objects.all() else None

