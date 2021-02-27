from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class CinemaViewsets(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = (IsAuthenticated,)


class CinemaDeckViewsets(viewsets.ModelViewSet):
    queryset = Cinema_Deck.objects.all()
    serializer_class = CinemaDeckSerializer
    permission_classes = (IsAuthenticated,)


class CinemaSlotsDurationViewsets(viewsets.ModelViewSet):
    queryset = CinemaSlotsDuration.objects.all()
    serializer_class = CinemaSlotsDurationSerializer
    permission_classes = (IsAuthenticated,)


class CinemaArrangeSlotViewsets(viewsets.ModelViewSet):
    queryset = CinemaArrangeSlot.objects.all()
    serializer_class = CinemaArrangeSlotWriteSerializer
    permission_classes = (IsAuthenticated,)
