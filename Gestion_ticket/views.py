from rest_framework import viewsets

from .serializers import *
from .models import *

# Create your views here.
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer