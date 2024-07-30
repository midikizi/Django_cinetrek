from rest_framework import serializers

from django.contrib.auth.hashers import make_password
from .models import Client, Gerant

class ClientSerializer(serializers.Serializer):
    class Meta:
        model = Client
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        password = validated_data['password']
        password = make_password(password)
        validated_data['password'] = password
        client = Client.objects.create(**validated_data)
        return client

    def update(self, instance, validated_data):
        instance['username'] = validated_data.get('username', instance.username)
        instance['password'] = validated_data.get('password', instance.password)
        instance['email'] = validated_data.get('email', instance.email)
        instance['first_name'] = validated_data.get('first_name', instance.first_name)
        instance['last_name'] = validated_data.get('last_name', instance.last_name)

        instance.save()
        return instance

class GerantSerializer(serializers.Serializer):
    class Meta:
        model = Gerant
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        password = validated_data['password']
        password = make_password(password)
        validated_data['password'] = password
        gerant = Gerant.objects.create(**validated_data)
        return gerant
    
    def update(self, instance, validated_data):
        instance['username'] = validated_data.get('username', instance.username)
        instance['password'] = validated_data.get('password', instance.password)
        instance['email'] = validated_data.get('email', instance.email)
        instance['first_name'] = validated_data.get('first_name', instance.first_name)
        instance['last_name'] = validated_data.get('last_name', instance.last_name)

        instance.save()
        return instance