# views.py
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .serialisers import *
from .models import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.pagination import PageNumberPagination
from datetime import date, timedelta
from rest_framework.parsers import MultiPartParser, FormParser
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
@parser_classes([MultiPartParser, FormParser])    
def post_item(request):
    serialiser = ItemSerialiser(data=request.data)
    if serialiser.is_valid():
        serialiser.save(owner=request.user)
        return Response(serialiser.data, status=status.HTTP_201_CREATED)
    return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def authentication_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({

            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user_id': user.id,
            'user_name' : user.username,
            'user_email': user.email
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'error' : 'invalid credentials'
        }, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET'])
def paginated_item_view(request):
    items = Item.objects.all()
    paginator = PageNumberPagination()
    itemised_page = paginator.paginate_queryset(items, request)
    serialiser = ItemSerialiser(itemised_page, many=True)
    return paginator.get_paginated_response(serialiser.data)

def available_dates(id):
    
    try:
        item = Item.objects.get(id=id)
    except:
        return Response({
            "error": f"Item with id {id} does not exist."
        }, status=status.HTTP_404_NOT_FOUND)
    
    todaydate = date.today()
    future_bookings = Booking.objects.filter(item=item, booking_end__gte=todaydate)
    dates_not_available = []
    for booking in future_bookings:
        start = todaydate
        end = booking.booking.end
        for i in range((end-start).days + 1):
            dates_not_available.append(start + timedelta(days=i))
    
    availability_range = [todaydate + timedelta(days=2) + timedelta(days=i) for i in range(60)]
    dates_available = [day for day in availability_range if date not in dates_not_available]

    return dates_available

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def item_page_view(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return Response({"error": f"Item {item_id} does not exist."}, status=404)

    image_urls = [
        request.build_absolute_uri(img.image.url)
        for img in item.images.all()
    ]

    dates_available = available_dates(item_id)

    return Response({
        "item_id": item.id,
        "user_id": item.owner.id,
        "username": item.owner.username,
        "item_name": item.title,
        "quantity": item.quantity,
        "dates_available": dates_available,
        "description": item.description,
        "images": image_urls       
    })