from django.urls import path, include
from django.contrib import admin

from TravelApp.accounts.views import LoginUserView, RegisterUserView, LogoutUserView, UserProfileView, EditProfileView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile view'),
    path('profile/<int:pk>/edit', EditProfileView.as_view(), name='edit profile')
)