from datetime import date, timedelta

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User  # noqa: F401 – kept for backward‑compat, but prefer get_user_model()
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    parser_classes,
    permission_classes,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import Booking, Item
from .serialisers import ItemSerialiser, UserSerialiser

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def _available_dates(item: Item, search_horizon_days: int = 60):
    """Return the list of dates *from tomorrow onwards* on which the item is free.

    The function looks at future bookings that overlap [today, today + horizon]
    and subtracts those days from the availability window.
    """
    today = date.today()
    tomorrow = today + timedelta(days=1)

    # All future bookings that still overlap with our search horizon
    future = Booking.objects.filter(item=item, booking_end__gte=today)

    unavailable = set()
    for b in future:
        # b.booking_start, b.booking_end are assumed; adjust field names if different
        for n in range((b.booking_end - b.booking_start).days + 1):
            unavailable.add(b.booking_start + timedelta(days=n))

    availability_window = [tomorrow + timedelta(days=i) for i in range(search_horizon_days)]
    return [d for d in availability_window if d not in unavailable]


# ---------------------------------------------------------------------------
# basic endpoints
# ---------------------------------------------------------------------------


@swagger_auto_schema(method="get", responses={200: openapi.Schema(type=openapi.TYPE_OBJECT)})
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def hello_view(request):
    """Quick sanity‑check endpoint for the frontend."""
    return Response({"message": "Hello, Vue frontend. From Django backend"})


@swagger_auto_schema(method="get", responses={200: UserSerialiser(many=True)})
@api_view(["GET"])
def user_list(request):
    users = get_user_model().objects.all()
    serializer = UserSerialiser(users, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method="get", responses={200: ItemSerialiser(many=True)})
@api_view(["GET"])
def item_list(request):
    items = Item.objects.all()
    serializer = ItemSerialiser(items, many=True)
    return Response(serializer.data)


# ---------------------------------------------------------------------------
# POST /post_item – create a new Item
# ---------------------------------------------------------------------------

_item_creation_responses = {
    201: ItemSerialiser,
    400: openapi.Schema(type=openapi.TYPE_OBJECT, description="Validation errors"),
}


@swagger_auto_schema(
    method="post",
    request_body=ItemSerialiser,
    responses=_item_creation_responses,
)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def post_item(request):
    serializer = ItemSerialiser(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---------------------------------------------------------------------------
# POST /authentication – issue JWT manually (if you do not use the built‑in view)
# ---------------------------------------------------------------------------

_auth_request_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=["username", "password"],
    properties={
        "username": openapi.Schema(type=openapi.TYPE_STRING),
        "password": openapi.Schema(type=openapi.TYPE_STRING, format="password"),
    },
)
_auth_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "access": openapi.Schema(type=openapi.TYPE_STRING),
        "refresh": openapi.Schema(type=openapi.TYPE_STRING),
        "user_id": openapi.Schema(type=openapi.TYPE_INTEGER),
        "user_name": openapi.Schema(type=openapi.TYPE_STRING),
        "user_email": openapi.Schema(type=openapi.TYPE_STRING, format="email"),
    },
)


@swagger_auto_schema(
    method="post",
    request_body=_auth_request_schema,
    responses={200: _auth_response_schema, 401: "Invalid credentials"},
)
@api_view(["POST"])
def authentication_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)

    if user is None:
        return Response({"error": "invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)
    return Response(
        {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user_id": user.id,
            "user_name": user.username,
            "user_email": user.email,
        },
        status=status.HTTP_200_OK,
    )


# ---------------------------------------------------------------------------
# GET /items – paginated item list
# ---------------------------------------------------------------------------


@swagger_auto_schema(method="get", responses={200: ItemSerialiser(many=True)})
@api_view(["GET"])
def paginated_item_view(request):
    items = Item.objects.all()
    paginator = PageNumberPagination()
    page = paginator.paginate_queryset(items, request)
    serializer = ItemSerialiser(page, many=True)
    return paginator.get_paginated_response(serializer.data)


# ---------------------------------------------------------------------------
# GET /item/<id> – item detail including availability
# ---------------------------------------------------------------------------

_item_id_param = openapi.Parameter(
    "item_id",
    openapi.IN_PATH,
    description="Primary key of the item",
    type=openapi.TYPE_INTEGER,
)


@swagger_auto_schema(method="get", manual_parameters=[_item_id_param], responses={200: ItemSerialiser})
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def item_page_view(request, item_id: int):
    item = get_object_or_404(Item, id=item_id)

    image_urls = [request.build_absolute_uri(img.image.url) for img in item.images.all()]
    dates_available = _available_dates(item)

    return Response(
        {
            "item_id": item.id,
            "user_id": item.owner.id,
            "username": item.owner.username,
            "item_name": item.title,
            "quantity": item.quantity,
            "dates_available": dates_available,
            "description": item.description,
            "images": image_urls,
        }
    )
