from django.urls import path
from .views import *

urlpatterns = [
    path('', frontpage, name='frontpage' ),
    path('', contact, name='contact' ),
]
