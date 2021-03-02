from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from managecinema.models import Cinema
from .models import *
from .serializers import *
from rest_framework.response import Response


# Create your views here.


class ReviewViewsets(generics.ListCreateAPIView):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
            cinema_query = Cinema.objects.get(id=request.data.get('movie'))
            cinema_query.all_review.add(data.id)
        return Response(serializer.data, status=200)
