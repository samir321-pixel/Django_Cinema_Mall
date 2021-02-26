from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response


# Create your views here.
class CinemaViewsets(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class CinemaDeckViewsets(viewsets.ModelViewSet):
    queryset = Cinema_Deck.objects.all()
    serializer_class = CinemaDeckSerializer


class CinemaSlotsDurationViewsets(viewsets.ModelViewSet):
    queryset = CinemaSlotsDuration.objects.all()
    serializer_class = CinemaSlotsDurationSerializer


class CinemaArrangeSlotViewsets(viewsets.ModelViewSet):
    queryset = CinemaArrangeSlot.objects.all()
    serializer_class = CinemaArrangeSlotWriteSerializer
