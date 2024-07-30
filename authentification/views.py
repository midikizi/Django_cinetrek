from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import *
from django.contrib.auth import authenticate

@api_view(["POST"])
def register_user_client(request):
    serializer = ClientSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        user = Client.objects.get(username=request.data['username'])
        token = Token.objects.get(user=user)

        serializer = ClientSerializer(user)
        data = {
            "user": serializer.data,
            "token": token.key
        }
        return Response(data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def register_user_gerant(request):
    serializer = GerantSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        user = Gerant.objects.get(username=request.data['username'])
        token = Token.objects.get(user=user)

        serializer = GerantSerializer(user)
        data = {
            "user": serializer.data,
            "token": token.key
        }
        return Response(data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def login_user(request):
    data = request.data
    authenticate_user = authenticate(username=data['username'], password=data['password'])

    if authenticate_user is not None:
        user = CustomUser.objects.get(username=data['username'])
        serializer = GerantSerializer(user) if user.is_gerant else ClientSerializer(user)
        response_data = { 'user': serializer.data }
        token, created = Token.objects.get_or_create(user=user)

        response_data['token'] = token.key
        return Response(response_data)
    return Response({"detail": "User Not found"}, status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def TestView(request): return Response({"message": "Test view page"})


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout_user(request):
    request.user.auth_token.delete()
    return Response({"message": "logout success"})
