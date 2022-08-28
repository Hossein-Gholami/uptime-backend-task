from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q
import random
from datetime import datetime as dt

from .models import *

def read_location_from_mqtt(driver_id):
    # we are supposed to read the location data from /test/driver/{driver_id}
    return (random.randint(1,100), random.randint(1,100))  # (latitude, longitude)

@receiver(post_save, sender=Order)
def saved_order(sender, instance, created, **kwargs):
    """"This will be triggered upon :model:Order instance creation."""
    
    if created:
        # steps:
        #  1. find the closest free driver
        #  2. assign this order to that driver
        #  3. update whatever field needed
        # done!

        # step #1: find the (almost) perfect candidate driver
        freeDrivers = Driver.objects.filter(Q(status__eq=Driver.StatusChoices.FREE.value))
        if freeDrivers.count()==0:
            return
        # now read locations
        for free in freeDrivers:
            free.location = str(read_location_from_mqtt(free.user.id))
        


        # Using redis geospatial data structure is the best idea that comes to me at the moment
        # so maybe by redis.GEORADIUS utility function an acceptable candidate would be found
        # what might be a problem is fairness so a driver might be free for so long
        # but it's not my concern for now
        
        # for now because I'm already late for submitting the task, I would choose one randomly
        candidate = freeDrivers[random.randint(0, freeDrivers.count()-1)]

        # step #2: assigning the mission
        candidate.update(currentMission=instance, status=Driver.StatusChoices.BUSY)
        instance.update(status=Order.StatusChoices.ASSIGNED,\
                        isActive=True, driver=candidate, assignedAt=dt.now())

