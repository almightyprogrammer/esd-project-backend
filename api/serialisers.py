from rest_framework import serializers
from .models import Item, User, Booking


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    

class BookingSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class ItemSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

