from rest_framework import serializers

from .models import *
from authentification.serializers import ClientSerializer
from Gestion_cinema.serializers import *

class TicketSerializer(serializers.ModelSerializer):
    salle = SalleSerializer()
    place = PlaceSerializer()
    seance = SalleSerializer()
    nomClient = ClientSerializer()

    class Meta:
        model = Ticket
        fields = ['id','nomClient','prix','codePayement','salle','place']