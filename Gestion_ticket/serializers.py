from rest_framework import serializers
from .models import *

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Ticket
        fields = '__all__'