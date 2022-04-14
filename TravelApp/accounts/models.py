from django.db import models

# Create your models here.
from django.urls import reverse

from static.countries_list import countries as COUNTRIES
from django.db import models
from django.contrib.auth import models as auth_models


# Create your models here.
from TravelApp.accounts.managers import ApplicationUserManager


class ApplicationUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    object = ApplicationUserManager()


class Profile(models.Model):
    COUNTRIES = COUNTRIES
    NAME_MAX_LENGTH = 200
    COUNTRY_CHOICES = [(x, x) for x in COUNTRIES]
    POSSIBLE_GENDERS = ['Male', 'Female', 'Undisclosed']
    GENDERS = [(x, x) for x in POSSIBLE_GENDERS]
    first_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    last_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    email = models.EmailField()

    country_of_residence = models.CharField(
        max_length=max(len(x) for x in COUNTRIES),
        choices=COUNTRY_CHOICES,
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x in POSSIBLE_GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
    )

    date_of_birth = models.DateField()

    user = models.OneToOneField(
        ApplicationUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @staticmethod
    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return f'{self.first_name} {self.last_name} from {self.country_of_residence} born on {self.date_of_birth}'

