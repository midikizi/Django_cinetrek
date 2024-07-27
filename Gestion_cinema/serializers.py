from rest_framework import serializers
from .models import *

class VilleSerializer(serializers.Serializer):
    class Meta:
        model = Ville
        fields = ()

    def create(self, validated_data):
        ville = Ville.objects.create(**validated_data)
        return ville
