from django.urls import path

from common.views import index, all_trips

urlpatterns = [
    path('', index, name='index'),
    path('all-trips/', all_trips, name='all_trips'),
]

