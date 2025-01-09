from django.urls import path, include

from trip.views import create_trip, details_trip, edit_trip, delete_trip

urlpatterns = [
    path('create/', create_trip, name='create_trip'),
    path('<int:trip_id>/', include([
        path('details/', details_trip, name='details_trip'),
        path('edit/', edit_trip, name='edit_trip'),
        path('delete/', delete_trip, name='delete_trip'),
    ]))
]