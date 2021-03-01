from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.response import Response


# Create your views here.
class NotificationListView(generics.ListAPIView):
    queryset = Notification.objects.all().order_by('-created_at')
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)
