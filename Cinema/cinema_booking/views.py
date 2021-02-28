from rest_framework import viewsets

from managecinema.models import CinemaArrangeSlot
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class AvailableSlotsViewsets(viewsets.ModelViewSet):
    queryset = Available_Slots.objects.all()
    serializer_class = AvailableSlotsReadSerializer


class SeatsViewsets(viewsets.ModelViewSet):
    queryset = Seat.objects.all().order_by('-date')
    filter_backends = [SearchFilter, ]
    serializer_class = SeatSerializer
    search_fields = ['name', 'deck__deck_name', 'date']

    def get_queryset(self):
        CinemaArrangeSlot.slot_updater(self=self)
        CinemaArrangeSlot.slot_maker(self=self)
        CinemaArrangeSlot.seat_maker(self=self)
        return Seat.objects.all().order_by('-date')


class BookSeatsViewsets(viewsets.ModelViewSet):
    queryset = BookSeat.objects.all().order_by('-created_at')
    serializer_class = BookSeatSerializer
