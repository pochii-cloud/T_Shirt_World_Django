from django.urls import path

from accounts.views import RegisterUser, LoginPage, LogoutPage

urlpatterns = [
    path('RegisterUser/', RegisterUser.as_view(), name='RegisterUser'),
    path('login/', LoginPage.as_view(), name='login'),
    path('LogoutPage/', LogoutPage.as_view(), name='LogoutPage'),
]
