from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth.hashers import make_password
from .models import Client, Gerant

class ClientSerializer(serializers.Serializer):
    class Meta:
        model = Client
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']

    def save(self, *args, **kwargs):
        client = Client.objects.create(
            username=self.validated_data['username'],
            password=make_password(self.validated_data['password']),
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        client.save()
        token = Token.objects.create(user=client)
        token.save()
        super().save(*args, **kwargs)

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
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']

    def save(self, *args, **kwargs):
        gerant = Gerant.objects.create(
            username=self.validated_data['username'],
            password=make_password(self.validated_data['password']),
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        gerant.save()
        token = Token.objects.create(user=gerant)
        token.save()
        super().save(*args, **kwargs)

    def update(self, instance, validated_data):
        instance['username'] = validated_data.get('username', instance.username)
        instance['password'] = validated_data.get('password', instance.password)
        instance['email'] = validated_data.get('email', instance.email)
        instance['first_name'] = validated_data.get('first_name', instance.first_name)
        instance['last_name'] = validated_data.get('last_name', instance.last_name)

        instance.save()
        return instance
