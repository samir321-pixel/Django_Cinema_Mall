from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response


# Create your views here.


class ReviewViewsets(generics.ListCreateAPIView):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)
