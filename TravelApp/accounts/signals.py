
from django.db.models import signals
from django.dispatch import receiver
from .models import Profile, Relationship


@receiver(signals.post_save, sender=Relationship)
def post_save_add_to_friends(sender, instance, created, **kwargs):
    sender_ = instance.sender
    receiver_ = instance.receiver
    if instance.status == 'accepted':
        sender_.friends.add(receiver_.user)
        receiver_.friends.add(sender_.user)
        sender_.save()
        receiver_.save()


@receiver(signals.pre_delete, sender=Relationship)
def pre_delete_remove_from_friends(sender, instance, **kwargs):
    sender_ = instance.sender
    receiver_ = instance.receiver
    sender_.friends.remove(receiver_.user)
    receiver_.friends.remove(sender_.user)
    sender_.save()
    receiver_.save()
