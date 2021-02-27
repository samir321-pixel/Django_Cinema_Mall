from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
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
    queryset = Cinema_Deck.objects.all()
    serializer_class = CinemaDeckSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Cinema_Deck.objects.all().order_by('-created_at')

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
            instance = Cinema_Deck.objects.get(id=self.kwargs["id"])
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
            instance = Cinema_Deck.objects.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)
        if self.request.user.is_admin or self.request.user.is_employee:
            instance.delete()
            return Response({"successful": "Access Granted"}, status=200)
        else:
            return Response({"error": "Access Denied"}, status=401)


class CinemaSlotsDurationViewsets(viewsets.ModelViewSet):
    queryset = CinemaSlotsDuration.objects.all()
    serializer_class = CinemaSlotsDurationSerializer
    permission_classes = (IsAuthenticated,)


class CinemaArrangeSlotViewsets(viewsets.ModelViewSet):
    queryset = CinemaArrangeSlot.objects.all()
    serializer_class = CinemaArrangeSlotWriteSerializer
    permission_classes = (IsAuthenticated,)
