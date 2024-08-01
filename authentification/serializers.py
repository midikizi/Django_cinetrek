from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth.hashers import make_password
from .models import Client, Gerant

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']

class GerantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gerant
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
