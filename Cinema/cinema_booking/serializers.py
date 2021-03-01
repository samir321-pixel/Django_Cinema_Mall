from rest_framework import serializers
from managecinema.serializers import CinemaDeckSerializer
from .models import *


class AvailableSlotsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Available_Slots
        fields = '__all__'
        depth = 2


class SeatSerializer(serializers.ModelSerializer):
    deck = CinemaDeckSerializer()

    class Meta:
        model = Seat
        fields = '__all__'
        depth = 1


class BookSeatSerializer(serializers.ModelSerializer):
    booking_price = serializers.CharField(max_length=200, allow_null=True)

    class Meta:
        model = BookSeat
        fields = '__all__'


class SeatManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = seat_manager
        fields = '__all__'
