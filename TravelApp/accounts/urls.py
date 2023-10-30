from django.urls import path, include
from django.contrib import admin

from TravelApp.accounts.views import LoginUserView, RegisterUserView, LogoutUserView, UserProfileView, edit_profile

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('<slug>/', UserProfileView.as_view(), name='profile view'),
    path('profile/<int:pk>/edit', edit_profile, name='edit profile')
)