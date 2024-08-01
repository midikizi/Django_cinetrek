from rest_framework import serializers
from .models import *

class CinemaSerializer(serializers.Serializer):
    class Meta:
        model = Cinema
        fields = '__all__'

class VilleSerializer(serializers.Serializer):
    class Meta:
        model = Ville
        fields = '__all__'

class CategorieSerializer(serializers.Serializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class FilmSerializer(serializers.Serializer):
    class Meta:
        model = Film
        fields = '__all__'

class PlaceSerializer(serializers.Serializer):
    class Meta:
        model = Place
        fields = '__all__'

class SalleSerializer(serializers.Serializer):
    class Meta:
        model = Salle
        fields = '__all__'

# class ProjectionSerializer(serializers.Serializer):
#     class Meta:
#         model = Projection
#         fields = '__all__'

class SeanceSerializer(serializers.Serializer):
    class Meta:
        model = Seance
        fields = '__all__'
