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
        blank=True,
    )

    last_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=True,
    )

    email = models.EmailField()

    profile_picture = models.ImageField()

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

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        ApplicationUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    friends = models.ManyToManyField(ApplicationUser, blank=True, related_name='friends')

    first_log_in = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('profile view', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class RelationshipManager(models.Manager):
    @staticmethod
    def invitations_received(receiver):
        qs = Relationship.objects.filter(receiver=receiver, status='sent')
        return qs


class Relationship(models.Model):
    STATUS_OPTIONS = [('sent', 'sent'),
                      ('accepted', 'accepted'),
                      ('rejected', 'rejected')]
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=max(max([len(y) for y in x]) for x in STATUS_OPTIONS), choices=STATUS_OPTIONS)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = RelationshipManager()

    def __str__(self):
        return f'{self.sender}-{self.receiver}-{self.status}'
