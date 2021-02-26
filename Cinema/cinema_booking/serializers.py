from rest_framework import serializers
from .models import *


class AvailableSlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Available_Slots
        fields = '__all__'
