from django.urls import path

from .views import *

urlpatterns = [
    path('ticket/create', create_ticket, name="ticket")
]
