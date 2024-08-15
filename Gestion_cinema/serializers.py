from rest_framework import serializers
from .models import *

class CinemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cinema
        fields = ['id','nom','nombreSalle','longitude','latitute','altitude']

class VilleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ville
        fields = ['id','nombreSalle','longitude','latitute','altitude','cinema']

class CategorieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'nom', 'description' ]

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ['id','titre','duree','realisateur','description','photo','dateSortie','category']

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ['id','numero','prix','reservee','libre']

class SalleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Salle
        fields = ['id', 'nom', 'nombrePlace','cinema','places' ]

class SeanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seance
        fields = ['id','date','prix','heureDebut','film']
