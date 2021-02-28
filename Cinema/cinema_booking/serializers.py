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


class BookSeatReadSerializer(serializers.ModelSerializer):
    seat = SeatSerializer()

    class Meta:
        model = BookSeat
        fields = '__all__'
        depth = 2


class BookSeatWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSeat
        fields = '__all__'
