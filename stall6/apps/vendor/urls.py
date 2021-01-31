from django.urls import path

from .views import Vendor

urlpatterns = [
    path('list/', Vendor, name='vendors-list'),
]
