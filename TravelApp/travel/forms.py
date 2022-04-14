from django import forms as django_forms

from TravelApp.travel.models import Trip


class CreateTripForm(django_forms.ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'

