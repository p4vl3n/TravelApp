from django.db.models import signals
from django.dispatch import receiver
from django.shortcuts import redirect
from django.urls import reverse_lazy

from TravelApp.accounts.models import ApplicationUser


@receiver(signals.pre_save, sender=ApplicationUser)
def user_created(instance, **kwargs):
    return reverse_lazy('create profile')