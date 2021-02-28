from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return BookSeat.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer = BookSeatSerializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            if self.request.user.is_admin or self.request.user.is_employee or self.request.user.is_customer:
                serializer.save(user=self.request.user)
                return Response({"Seat Booked": "Access Granted"})
            else:
                return Response({"NO_ACCESS": "Access Denied"}, status=401)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, *args, **kwargs):
        if self.request.user.is_admin or self.request.user.is_employee or self.request.user.is_customer:
            try:
                queryset = BookSeat.objects.get(id=self.kwargs["id"])
                serializer = BookSeatSerializer(queryset)
                return Response(serializer.data, status=200)
            except:
                return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=401)

    def perform_update(self, serializer):
        queryset = BookSeat.objects.get(id=self.kwargs["id"])
        if self.request.user.is_admin or self.request.user.is_employee:
            serializer = BookSeatSerializer(queryset, data=self.request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                serializer = BookSeatSerializer(queryset)
                return Response(serializer.data, status=200)
            return Response({"NO_ACCESS": "Access Denied"}, status=401)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=401)

    def perform_destroy(self, instance):
        if self.request.user.is_admin or self.request.user.is_employee:
            try:
                instance = BookSeat.objects.get(id=self.kwargs["id"])
                instance.delete()
                return Response({"Seat Deleted": "Access Granted"}, status=204)
            except:
                return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=401)
