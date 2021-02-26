from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response


# Create your views here.
class AvailableSlotsViewsets(viewsets.ModelViewSet):
    queryset = Available_Slots.objects.all()
    serializer_class = AvailableSlotsSerializer
