from django.db import models

# Create your models here.
from django.db import models

from TravelApp.accounts.models import ApplicationUser, Profile
from static.countries_list import countries as COUNTRIES

# Create your models here.


class Trip(models.Model):
    COUNTRIES = COUNTRIES
    COUNTRY_CHOICES = [(x, x) for x in COUNTRIES]

    duration = models.PositiveIntegerField()

    destination = models.CharField(
        max_length=365,
        choices=COUNTRY_CHOICES,
    )

    departure_date = models.DateField()

    departure_time = models.TimeField()

    travellers = models.ManyToManyField(
        Profile,
        blank=True,
    )

    added_by = models.ForeignKey(ApplicationUser, on_delete=models.CASCADE)

    important_files = models.FileField(upload_to='uploads/', blank=True)

    trip_pictures = models.ImageField(upload_to='mediafiles/', blank=True, default=None)

    on_wishlist = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.duration} trip to {self.destination}'


class TripDay(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    day_number = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f'Day {self.day_number} of the trip to {self.trip.destination}'


class Image(models.Model):
    description = models.TextField()
    image = models.ImageField()
    day = models.ForeignKey(TripDay, on_delete=models.CASCADE)

#
# class WishTrip(Trip):
#     wishlist = True
