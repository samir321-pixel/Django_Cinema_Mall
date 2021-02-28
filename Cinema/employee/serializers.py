from .models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    salary = serializers.CharField(max_length=200)

    class Meta:
        model = Employee
        fields = '__all__'
