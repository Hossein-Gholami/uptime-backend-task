from django.urls import path
from . import views

app_name = 'uptime'

driver_urlpatterns = [
    path('drivers/', views.DriverList.as_view()),
    path('drivers/<int:pk>', views.DriverDetail.as_view()),
]

order_urlpatterns = [
    path('orders/', views.OrderList.as_view()),
    path('orders/<int:pk>', views.OrderDetail.as_view()),
]

urlpatterns = driver_urlpatterns + order_urlpatterns

