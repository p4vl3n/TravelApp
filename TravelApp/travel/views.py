from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from django.shortcuts import render
import django.views.generic as views

# Create your views here.
from TravelApp.accounts.models import Profile, ApplicationUser
from TravelApp.travel.forms import FriendSearchForm, CreateTripForm
from TravelApp.travel.models import Trip, TripDay, Image


class HomeView(views.TemplateView):
    template_name = 'home.html'


class CreateWishTrip(views.CreateView):
    pass


class UserWishlist(views.ListView):
    model = Trip
    template_name = 'travel/user_wishlist.html'

    def get_queryset(self):
        trips = Trip.objects.filter(added_by=self.request.user, on_wishlist=True)
        return trips
    # def get_context_object_name(self, *, object_list=None, **kwargs):
    #     queryset


class CreateTrip(views.CreateView):
    model = Trip
    template_name = 'travel/create_trip.html'
    success_url = reverse_lazy('user trips')
    # fields = ('duration',
    #           'destination',
    #           'departure_date',
    #           'departure_time',
    #           'travellers',
    #           'important_files',
    #           'trip_pictures',
    #           )
    form_class = CreateTripForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.added_by = self.request.user
        self.object.save()
        result = super().form_valid(form)
        duration = form.cleaned_data.get('duration')
        a = 5
        for day in range(duration):
            trip_day = TripDay(trip=form.instance,
                               day_number=day+1)
            trip_day.save()
        return HttpResponseRedirect(self.get_success_url())


class UserTrips(views.ListView):
    model = Trip
    template_name = 'travel/user_trips.html'

    def get_queryset(self):
        trips = Trip.objects.filter(added_by=self.request.user)
        return trips

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DeleteTrip(views.DeleteView):
    model = Trip
    template_name = 'travel/delete_trip.html'


class FriendSearch(views.ListView):
    model = Profile
    template_name = 'travel/friend_search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        try:
            first_name, last_name = query.split()
        except ValueError:
            first_name = query
            last_name = query

        object_list = Profile.objects.filter(
            Q(first_name__icontains=first_name) | Q(last_name__icontains=last_name)
        )
        return object_list


class TripDetailView(views.DetailView):
    model = Trip
    template_name = 'travel/trip_details.html'
    context_object_name = 'trip'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        travellers = self.object.travellers.all()
        days = TripDay.objects.filter(trip_id=self.object.id).order_by('day_number')
        context['travel_buddies'] = travellers
        context['days'] = days
        return context


class DayDetailView(views.DetailView):
    model = TripDay
    template_name = 'travel/day_details.html'
    context_object_name = 'day'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pictures = Image.objects.filter(day_id=self.object.id)
        context['pictures'] = pictures
        return context


class EditDayView(views.UpdateView):
    model = TripDay
    template_name = 'travel/edit_day.html'
    fields = ('description', )

    def get_success_url(self):
        return reverse_lazy('trip details', kwargs={'pk': self.object.trip_id})

    def post(self, request, *args, **kwargs):
        images = request.FILES.getlist('images')
        photo_description = request.POST['photo description']
        for image in images:
            photo = Image.objects.create(
                description=photo_description,
                image=image,
                day=self.model.objects.get(id=kwargs['pk'])
            )
        return super().post(request, *args, **kwargs)


