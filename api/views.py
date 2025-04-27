from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .serialisers import *
from .models import *
User = get_user_model()

@api_view(['GET'])
def hello_view(request):
    return Response({"message": "Hello, Vue frontend. From Django backend"})

@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serialiser = UserSerialiser(users, many=True)
    return Response(serialiser.data)

@api_view(['GET'])
def item_list(request):
    items = Item.objects.all()
    serialiser = ItemSerialiser(items, many=True)
    return Response(serialiser.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def post_item(request):
    serialiser = ItemSerialiser(data=request.data)
    if serialiser.is_valid():
        serialiser.save(owner=request.user)
        return Response(serialiser.data, status=status.HTTP_201_CREATED)
    return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)
