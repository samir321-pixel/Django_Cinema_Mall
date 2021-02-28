from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from managecinema.models import CinemaArrangeSlot
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.core.exceptions import ObjectDoesNotExist


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
        Seat.seat_updater(self=self)
        return Seat.objects.all().order_by('-date')


class BookSeatsViewsets(viewsets.ModelViewSet):
    queryset = BookSeat.objects.all().order_by('-created_at')
    serializer_class = BookSeatReadSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return BookSeat.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer = BookSeatWriteSerializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            if self.request.user.is_admin or self.request.user.is_employee or self.request.user.is_customer:
                serializer.save(user=self.request.user)
                Seat.seat_book(self=self, seat=self.request.data.get('seat'), user=self.request.user)
                return Response(serializer.data, status=200)
            else:
                return Response({"NO_ACCESS": "Access Denied"}, status=401)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, *args, **kwargs):
        if self.request.user.is_admin or self.request.user.is_employee or self.request.user.is_customer:
            try:
                queryset = BookSeat.objects.get(id=self.kwargs["id"])
                serializer = BookSeatReadSerializer(queryset)
                return Response(serializer.data, status=200)
            except:
                return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=401)

    def perform_update(self, serializer):
        # only admin or employee will be able to update and delete
        queryset = BookSeat.objects.get(id=self.kwargs["id"])
        if self.request.user.is_admin or self.request.user.is_employee:
            serializer = BookSeatWriteSerializer(queryset, data=self.request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(updated_at=datetime.now())
                serializer = BookSeatReadSerializer(queryset)
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


class SeatManagerViewsets(viewsets.ModelViewSet):
    queryset = seat_manager.objects.all().order_by('-created_at')
    serializer_class = SeatManagerSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return seat_manager.objects.all()

    def perform_create(self, serializer):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            if self.request.user.is_admin or self.request.user.is_employee:
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response({"NO_ACCESS": "Access Denied"}, status=401)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, *args, **kwargs):
        if self.request.user.is_admin or self.request.user.is_employee:
            try:
                queryset = seat_manager.objects.get(id=self.kwargs["id"])
                serializer = self.get_serializer(queryset)
                return Response(serializer.data, status=200)
            except ObjectDoesNotExist:
                return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=401)

    def update(self, request, *args, **kwargs):
        try:
            if self.request.user.is_admin or self.request.user.is_employee:
                try:
                    queryset = seat_manager.objects.get(id=self.kwargs["id"])
                    serializer = self.get_serializer(queryset, data=self.request.data, partial=True)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save(updated_at=datetime.now())
                        return Response(serializer.data, status=200)
                    else:
                        return Response(serializer.errors, status=400)
                except ObjectDoesNotExist:
                    return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)
        except:
            return Response({"NO_ACCESS": "Access Denied"}, status=401)

    def perform_destroy(self, instance):
        if self.request.user.is_admin or self.request.user.is_superuser:
            try:
                queryset = seat_manager.objects.get(id=self.kwargs["id"])
                queryset.delete()
                return Response({"Successful": "successful"}, status=204)
            except ObjectDoesNotExist:
                return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=401)
