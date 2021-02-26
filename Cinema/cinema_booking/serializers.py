from rest_framework import serializers
from .models import *


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Available_Slots
        fields = '__all__'
