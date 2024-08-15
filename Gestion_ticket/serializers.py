from rest_framework import serializers
from .models import *

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id','nomClient','prix','codePayement','salle','place']