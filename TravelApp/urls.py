from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from TravelApp.travel.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('TravelApp.accounts.urls')),
    path('travel/', include('TravelApp.travel.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)