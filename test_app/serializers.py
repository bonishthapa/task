from rest_framework import serializers
from test_app.models import Department,Employee


class EmployeeSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Employee
        fields = ['id','name','address','image','department']

class DepartmentSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=True,read_only=True)
    class Meta:
        model = Department
        fields=['id','name','employee']
