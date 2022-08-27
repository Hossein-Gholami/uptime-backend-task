from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q

from .models import *


@receiver(post_save, sender=Order)
def saved_order(sender, instance, created, **kwargs):
    """"This will be triggered every time a :model:Order instance is saved."""
    
    if created:
        pass
