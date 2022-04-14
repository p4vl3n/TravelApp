from django.shortcuts import render

# Create your views here.
from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.shortcuts import render
import django.views.generic as views

# Create your views here.
from TravelApp.travel.models import Trip


class HomeView(views.TemplateView):
    template_name = 'home.html'


# class SomeClass(auth_mixin.LoginRequiredMixin, views.DetailView):
#     # model = PetPhoto
#     # template_name = 'main/photo_details.html'
#     # context_object_name = 'pet_photo'
#
#     def dispatch(self, request, *args, **kwargs):
#         response = super().dispatch(request, *args, **kwargs)
#
#         viewed_pet_photos = request.session.get('last_viewed_pet_photo_ids', [])
#
#         viewed_pet_photos.insert(0, self.kwargs['pk'])
#         request.session['last_viewed_pet_photo_ids'] = viewed_pet_photos[:4]
#
#         return response


class UserTrips(views.ListView):
    model = Trip
    template_name = 'travel/user_trips.html'

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class UserWishlist(views.TemplateView):
    template_name = 'travel/user_wishlist.html'


class CreateTrip(views.CreateView):
    model = Trip
    template_name = 'travel/create_trip.html'
    success_url = reverse_lazy('user trips')
    fields = '__all__'

    # def post(self, request, *args, **kwargs):
    #     super().post(request, *args, **kwargs)
    #     return render(request, 'travel/user_trips.html')

    def form_valid(self, form):
        result = super().form_valid(form)
        result.save()
        return result
