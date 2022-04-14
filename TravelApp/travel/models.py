from django.db import models

# Create your models here.
from django.db import models

from TravelApp.accounts.models import ApplicationUser
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

    travellers = models.ManyToManyField(
        ApplicationUser,
    )

