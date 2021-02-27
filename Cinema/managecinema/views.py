from rest_framework import viewsets
from rest_framework.response import Response
from cinema_booking.models import Seat
from cinema_booking.models import Available_Slots
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist


class CinemaViewsets(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Cinema.objects.all().order_by('-created_at')

    def create(self, request, *args, **kwargs):
        if self.request.user.is_admin or self.request.user.is_employee:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=401)

    def update(self, request, *args, **kwargs):
        try:
            instance = Cinema.objects.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)
        if self.request.user.is_admin or self.request.user.is_employee:
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response({"error": "Access Denied"}, status=401)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = Cinema.objects.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)
        if self.request.user.is_admin or self.request.user.is_employee:
            instance.delete()
            return Response({"successful": "Access Granted"}, status=200)
        else:
            return Response({"error": "Access Denied"}, status=401)


class CinemaDeckViewsets(viewsets.ModelViewSet):
    queryset = CinemaDeck.objects.all()
    serializer_class = CinemaDeckSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return CinemaDeck.objects.all().order_by('-created_at')

    def create(self, request, *args, **kwargs):
        if self.request.user.is_admin or self.request.user.is_employee:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=401)

    def update(self, request, *args, **kwargs):
        try:
            instance = CinemaDeck.objects.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)
        if self.request.user.is_admin or self.request.user.is_employee:
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response({"error": "Access Denied"}, status=401)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = CinemaDeck.objects.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)
        if self.request.user.is_admin or self.request.user.is_employee:
            instance.delete()
            return Response({"successful": "Access Granted"}, status=200)
        else:
            return Response({"error": "Access Denied"}, status=401)


class CinemaSlotsDurationViewsets(viewsets.ModelViewSet):
    queryset = MovieDurationSlot.objects.all()
    serializer_class = MovieDurationSlotSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return MovieDurationSlot.objects.all().order_by('-created_at')

    def create(self, request, *args, **kwargs):
        if self.request.user.is_admin or self.request.user.is_employee:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=401)

    def update(self, request, *args, **kwargs):
        try:
            instance = MovieDurationSlot.objects.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)
        if self.request.user.is_admin or self.request.user.is_employee:
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response({"error": "Access Denied"}, status=401)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = MovieDurationSlot.objects.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)
        if self.request.user.is_admin or self.request.user.is_employee:
            instance.delete()
            return Response({"successful": "Access Granted"}, status=200)
        else:
            return Response({"error": "Access Denied"}, status=401)


class CinemaArrangeSlotViewsets(viewsets.ModelViewSet):
    queryset = CinemaArrangeSlot.objects.all().order_by('created_at')
    serializer_class = CinemaArrangeSlotWriteSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        serializer = CinemaArrangeSlotReadSerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=200)

    def create(self, request, *args, **kwargs):
        if self.request.user.is_admin or self.request.user.is_employee:
            serializer = CinemaArrangeSlotWriteSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                data = serializer.save(active=True)
                query = MovieDurationSlot.objects.get(id=(request.data.get('duration_slot')))
                get_query = CinemaArrangeSlot.objects.get(id=data.id)
                fulldate = datetime.datetime(100, 1, 1, (get_query.start_time).hour, (get_query.start_time).minute,
                                             (get_query.start_time).second)
                next_time = fulldate + datetime.timedelta(seconds=(query.duration).seconds)
                get_query.end_time = next_time.time()
                get_query.save()
                if data:
                    CinemaArrangeSlot.slot_updater(self=self)
                    CinemaArrangeSlot.slot_maker(self=self)
                    CinemaArrangeSlot.seat_maker(self=self)
                serializer = CinemaArrangeSlotReadSerializer(get_query)
            return Response(serializer.data, status=200)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=401)

    def update(self, request, *args, **kwargs):
        try:
            instance = CinemaArrangeSlot.objects.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)
        if self.request.user.is_admin or self.request.user.is_employee:
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response({"error": "Access Denied"}, status=401)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = CinemaArrangeSlot.objects.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)
        if self.request.user.is_admin or self.request.user.is_employee:
            instance.delete()
            return Response({"successful": "Access Granted"}, status=200)
        else:
            return Response({"error": "Access Denied"}, status=401)
