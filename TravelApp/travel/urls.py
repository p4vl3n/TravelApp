from django.contrib import admin
from django.urls import path, include

from TravelApp.travel.views import UserTrips, UserWishlist, CreateTrip

urlpatterns = (
    path('trips/', UserTrips.as_view(), name='user trips'),
    path('wishlist/', UserWishlist.as_view(), name='user wishlist'),
    path('create/', CreateTrip.as_view(), name='create trip'),
)