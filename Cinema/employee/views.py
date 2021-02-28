from django.shortcuts import render

from user.models import User
from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class CreateEmployee(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        if request.user.is_admin or self.request.user.is_superuser:
            serializer = self.get_serializer(data=request.data)
            user_query = User.objects.get(id=request.data.get('user'))
            user_query.is_employee = True
            user_query.save()
            if serializer.is_valid(raise_exception=True):
                serializer.save(first_Name=user_query.first_name, last_Name=user_query.last_name)
            return Response(serializer.data, status=200)
