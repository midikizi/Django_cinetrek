from rest_framework.response import Response

from .serializers import *
from .models import *
# Create your views here.
def create_ville(request):
    ville = VilleSerializer(data=request.data)
    if ville.is_valid():
        serializers = ville.save()
    return Response({})