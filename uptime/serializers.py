from rest_framework import serializers
from . import models


class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Driver
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Order
        fields = '__all__'
