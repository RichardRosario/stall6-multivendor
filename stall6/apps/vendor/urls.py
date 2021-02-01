from django.urls import path

from .views import *

urlpatterns = [
    path('list/', vendorsList, name='vendors-list'),
    path('create_vendor/', createVendor, name='create-vendor'),
]
