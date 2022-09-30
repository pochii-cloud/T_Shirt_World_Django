from django.urls import path

from orders.views import MyOrders, CancelOrder

urlpatterns = [
    path('Myorders', MyOrders.as_view(), name='MyOrders'),
    path('CancelOrder/<int:pk>/', CancelOrder.as_view(), name='CancelOrder'),
    # path('UpdateOrder/<int:pk>/', UpdateOrder.as_view(), name='UpdateOrder')
]
