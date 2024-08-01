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

<<<<<<< HEAD
# class ProjectionSerializer(serializers.Serializer):
#     class Meta:
#         model = Projection
#         fields = '__all__'

class SeanceSerializer(serializers.Serializer):
=======
class SeanceSerializer(serializers.HyperlinkedModelSerializer):
>>>>>>> 1b03d19b5d0195e42e25cb7830cc5966d0f53179
    class Meta:
        model = Seance
        fields = '__all__'
