from django.contrib import admin

from .models import *

# Register your models here.

class DriverAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'longtitude', 'altitude', 'status', ]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'src', 'dest', 'status',\
        'isActive', 'createdAt', 'assignedAt', 'assignedTo', 'deliveredAt', ]

admin.site.register(Driver, DriverAdmin)
admin.site.register(Order)
