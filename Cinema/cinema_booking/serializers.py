from rest_framework import serializers
from .models import *


class AvailableSlotsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Available_Slots
        fields = '__all__'
        depth = 2
