from rest_framework import serializers
from .models import *

class CinemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'

class VilleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ville
        fields = '__all__'

class CategorieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class SalleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Salle
        fields = '__all__'

class SeanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seance
        fields = '__all__'
