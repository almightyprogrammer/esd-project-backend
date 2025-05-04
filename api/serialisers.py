from rest_framework import serializers
from .models import Item, User, Booking, ItemImage


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    

class BookingSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class ItemImageSerialiser(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ['id', 'image']




class ItemSerialiser(serializers.ModelSerializer):
    images = ItemImageSerialiser(many=True, read_only=True)
    uploaded_images = serializers.ListField(
           child=serializers.ImageField(), write_only = True, required = False
    )

    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ('owner', 'created_at')

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        item = Item.objects.create(**validated_data)
        for image in uploaded_images:
            ItemImage.objects.create(item=item, image=image)
        return item
    
