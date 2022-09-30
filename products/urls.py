from django.urls import path

from products.views import ProductDetails, CategoryDetail, ProductsPage

urlpatterns = [
    path('ProductDetails/<int:pk>/', ProductDetails.as_view(), name='ProductDetails'),
    path('CategoryDetail/<int:pk>/', CategoryDetail.as_view(), name='CategoryDetail'),
    path('ProductsPage/', ProductsPage.as_view(), name='ProductsPage')
]
