from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status 

from django.shortcuts import get_object_or_404
from .serializers import ClientSerializer
from .models import Client

# Create your views here.
@api_view(['POST'])
def logout_user(request):
    if request.method == 'POST':
        request.user.auth.token.delete()
        return Response({"message": "User logged out"}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user_client(request):
    clientSerializer = ClientSerializer(data=request.data)
    if clientSerializer.is_valid():
        email = clientSerializer.validate_data['email']
        username = clientSerializer.validate_data['username']
        if Client.objects.filter(email=email).exists():
            return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)
        if Client.objects.filter(username=username).exists():
            return Response({'error': 'Username already taken'}, status=status.HTTP_400_BAD_REQUEST)
        
        client = clientSerializer.save()
        return Response({
            'response': 'Client account created successfully',
            'username': client.username,
            'email': client.email,
            'token': client.auth_token.key
        }, status=status.HTTP_201_CREATED)
    else:
        return Response(clientSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    user = get_object_or_404(Client, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Utilisateur non trouve"}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = ClientSerializer(instance=user)
    return Response({"token": token, "user": serializer.data})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response(f"Succes pour {request.user.email}.")