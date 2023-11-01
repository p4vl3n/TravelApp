from django.contrib import admin
from django.urls import path, include

from TravelApp.travel.views import UserTrips, UserWishlist, CreateTrip, FriendSearch, TripDetailView, DayDetailView, \
     EditDayView, DeleteTrip

urlpatterns = (
    path('trips/', UserTrips.as_view(), name='user trips'),
    path('delete-trip/<int:pk>/', DeleteTrip.as_view(), name='delete trip'),
    path('create/', CreateTrip.as_view(), name='create trip'),
    path('wishlist/', UserWishlist.as_view(), name='user wishlist'),
    path('wishlist/add/', CreateTrip.as_view(), name='add to wishlist'),
    path('search/', FriendSearch.as_view(), name='friend search'),
    path('details/<int:pk>/', TripDetailView.as_view(), name='trip details'),
    path('day-details/<int:pk>/', DayDetailView.as_view(), name='day details'),
    path('edit-day/<int:pk>/', EditDayView.as_view(), name='edit day'),

)