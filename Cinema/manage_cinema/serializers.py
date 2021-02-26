from rest_framework import serializers
from .models import *


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'


class CinemaDeckSerializer(serializers.ModelSerializer):
    price = serializers.CharField(max_length=200)

    class Meta:
        model = Cinema_Deck
        fields = '__all__'


class CinemaSlotsDurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaSlotsDuration
        fields = '__all__'


class CinemaArrangeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaArrangeSlot
        fields = '__all__'
        depth = 1
