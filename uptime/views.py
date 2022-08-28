from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.db.models import Q

from .models import *
from .serializers import *

# Create your views here.

class DriverList(APIView):
    """"List all Drivers, or create a new one"""
    
    serializer_class = DriverSerializer

    permission_classes = (permissions.IsAdminUser, )
    http_method_names = ['get', 'post']

    def get(self, request):
        results = Driver.objects.all()
        serializer = self.serializer_class(results, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DriverDetail(APIView):
    """"Retrieve, update or delete a driver instance"""
    serializer_class = DriverSerializer

    permission_classes = (permissions.IsAdminUser, )
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_object(self, pk):
        try:
            return Driver.objects.get(pk=pk)
        except Driver.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        driver = self.get_object(pk=pk)
        serializer = self.serializer_class(driver)
        return Response(serializer.data)

    def put(self, request, pk):
        driver = self.get_object(pk=pk)
        serializer = self.serializer_class(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def delete(self, request, pk):
        driver = self.get_object(pk)
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderList(APIView):
    """"List all Orders, or create a new one"""
    
    serializer_class = OrderSerializer

    permission_classes = (permissions.IsAdminUser, )
    http_method_names = ['get', 'post']

    def get(self, request):
        results = Order.objects.all()
        serializer = self.serializer_class(results, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetail(APIView):
    """"Retrieve, update or delete an order instance"""
    serializer_class = OrderSerializer

    permission_classes = (permissions.IsAdminUser, )
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Driver.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        order = self.get_object(pk=pk)
        serializer = self.serializer_class(order)
        return Response(serializer.data)

    def put(self, request, pk):
        order = self.get_object(pk=pk)
        serializer = self.serializer_class(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request, pk):
    #     order = self.get_object(pk=pk)
    #     serializer = self.serializer_class(order, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def delete(self, request, pk):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FreeDrivers(APIView):
    """"This will result in a :QuerySet:Drivers who are free at the moment"""
    
    queryset = Driver.objects.filter(Q(status__eq=Driver.StatusChoices.FREE.value))
    serializer_class = DriverSerializer

    permission_classes = (permissions.IsAuthenticated, )
    http_method_names = ['get']

    def get(self, request):
        results = self.queryset.all()
        serializer = self.serializer_class(results, many=True)
        return Response(serializer.data)


class MissionsList(APIView):
    """"Lists all missions of a driver in present and past"""
    
    query_set = Order.objects.none()
    serializer_class = OrderSerializer

    permission_classes = (permissions.IsAuthenticated, )
    http_method_names = ['get']

    def get(self, request, pk):
        results = Order.objects.filter(Q(driver__user__id__eq=pk)).all()
        serializer = self.serializer_class(results, many=True)
        return Response(serializer.data)

class Delivered(APIView):
    """After delivery, this endpoint is called to do some queries"""
    
    queryset = Driver.objects.none()
    serializer_class = Driver

    permission_classes = (permissions.IsAuthenticated, )
    http_method_names = ['post']

    def post(self, request, pk):
        driver = Driver.objects.get(pk=pk)
        from datetime import datetime as dt
        driver.currentMission.update(deliveredAt=dt.now(), isActive=False, status=Order.StatusChoices.DELIVERED)
        driver.update(status=Driver.StatusChoices.FREE, currentMission=None)
        serializer = self.serializer_class(driver, data=request.data)
        return Response(serializer.data)
