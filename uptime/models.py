from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4

# Create your models here.

class Driver(AbstractUser):
    """"User model for driver"""
    
    class StatusChoices(models.IntegerChoices):
        BUSY = 1, "Busy"
        FREE = 0, "Free"

    name = models.CharField(max_length=255, null=True, blank=True)
    long = models.DecimalField(name="longtitude", max_digits=8, decimal_places=3, null=True)
    alt = models.DecimalField(name="altitude", max_digits=8, decimal_places=3, null=True)
    status = models.IntegerField(default=StatusChoices.FREE, choices=StatusChoices.choices)




class Order(models.Model):
    """"Order model"""
    
    class StatusChoices(models.IntegerChoices):
        TO_ASSIGN = 0, "TO_ASSIGN"
        ASSIGNED = 1, "ASSIGNED"
        DELIVERED = 2, "DELIVERED"

    # _id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    src = models.CharField(max_length=100, null=False, blank=False)
    dest = models.CharField(max_length=100, null=False, blank=False)
    status = models.IntegerField(default=StatusChoices.TO_ASSIGN, choices=StatusChoices.choices)
    active = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True, null=False)
    assignedAt = models.DateTimeField(auto_now_add=False, null=True)
    assignedTo = models.ForeignKey(to=Driver, on_delete=models.CASCADE, null=True)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True)
