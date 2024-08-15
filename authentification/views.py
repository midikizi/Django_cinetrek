from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
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
@permission_classes([AllowAny])
def register_user_client(request):
    serializer = ClientSerializer(data=request.data)

    if serializer.is_valid():
        client = serializer.save()
        token, created = Token.objects.get_or_create(user=client)

        return Response({
            "token": token.key,
            "user": serializer.data
        }, status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([AllowAny])
def register_user_gerant(request):
    serializer = GerantSerializer(data=request.data)

    if serializer.is_valid():
        gerant = serializer.save()
        token, created = Token.objects.get_or_create(user=gerant)

        return Response({
            "token": token.key,
            "user": serializer.data
        }, status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username', None)
    password = request.data.get('password', None)
    
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = ClientSerializer(user)
    
    return Response({
        'token': token.key,
        'user': serializer.data
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response("You have accessed a protected endpoint", status=status.HTTP_200_OK)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout_user(request):
    try:
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)