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
