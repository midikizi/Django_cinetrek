from rest_framework import serializers
from .models import *

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ['id','nom','nombreSalle','longitude','latitute','altitude','ville']

class VilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ville
        fields = ['id','nom','longitude','latitute','altitude']

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'nom', 'description' ]

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id','titre','duree','realisateur','description','photo','dateSortie','category']

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id','numero','prix','reservee','libre']

class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = ['id', 'nom', 'nombrePlace','cinema','places' ]

class SeanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seance
        fields = ['id','date','prix','heureDebut','film']
