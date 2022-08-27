from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4
from typing import Tuple

# Create your models here.

class Driver(models.Model):
    """"User model for driver"""
    
    class StatusChoices(models.IntegerChoices):
        BUSY = 1, "Busy"
        FREE = 0, "Free"
    # or Status = models.IntegerChoices('Status', 'Free Busy')

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, null=True)
    status = models.IntegerField(default=StatusChoices.FREE, choices=StatusChoices.choices)

    def __str__(self) -> str:
        return (f"<user: {self.user.username}> "
                f"<location: {self.location}> | status: { Driver.StatusChoices(self.status).label }")
    
    def update_location(self, loc: Tuple[int, int]):
        self.location = str(loc)

class Order(models.Model):
    """"Order model"""
    
    class StatusChoices(models.IntegerChoices):
        WAITING = 0, "Waiting"
        ASSIGNED = 1, "Assigned"
        DELIVERED = 2, "Delivered"

    # _id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    src = models.CharField(max_length=100, null=False, blank=False)
    dest = models.CharField(max_length=100, null=False, blank=False)
    status = models.IntegerField(default=StatusChoices.WAITING, choices=StatusChoices.choices)
    isActive = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True, null=False)
    assigned = models.ForeignKey(to=Driver, on_delete=models.CASCADE, null=True)
    assignedAt = models.DateTimeField(auto_now_add=False, null=True)
    delivered = models.DateTimeField(auto_now_add=False, null=True)

    def __str__(self):
        return (f"<from: {self.src}, to: {self.dest}> | status: { Order.StatusChoices(self.status).label }")


class Assignment(models.Model):
    driver = models.ForeignKey(to=Driver, on_delete=models.CASCADE, unique=True, null=False)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, null=False)
