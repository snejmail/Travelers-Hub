from django.urls import path

from traveler.views import create_traveler, details_traveler, edit_traveler, delete_traveler

urlpatterns = [
    path('create/', create_traveler, name='create_traveler'),
    path('details/', details_traveler, name='details_traveler'),
    path('edit/', edit_traveler, name='edit_traveler'),
    path('delete/', delete_traveler, name='delete_traveler'),
]