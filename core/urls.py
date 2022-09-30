from django.urls import path

from core.views import Homepage, AboutUs, ContactUs, SearchResults

urlpatterns = [
    path('', Homepage.as_view(), name='Homepage'),
    path('AboutUs/', AboutUs.as_view(), name='AboutUs'),
    path('ContactUs/', ContactUs.as_view(), name='ContactUs'),
    path('SearchResults/', SearchResults.as_view(), name='SearchResults'),
]
