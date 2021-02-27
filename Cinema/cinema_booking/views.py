from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response


# Create your views here.
class AvailableSlotsViewsets(viewsets.ModelViewSet):
    queryset = Available_Slots.objects.all()
    serializer_class = AvailableSlotsReadSerializer


class SeatsViewsets(viewsets.ModelViewSet):
    queryset = Seat.objects.all().order_by('-date')
    serializer_class = SeatSerializer