from cinema_booking.serializers import BookSeatSerializer
from .models import *
from rest_framework import serializers


class NotificationSerializer(serializers.ModelSerializer):
    seat = BookSeatSerializer()

    class Meta:
        model = Notification
        fields = '__all__'
