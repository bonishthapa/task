from django.shortcuts import render
from rest_framework import status,viewsets
from django.http.response import JsonResponse
from rest_framework.decorators import api_view, action
from rest_framework.parsers import JSONParser,ParseError
from test_app.models import Department, Employee
from test_app.serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.

@api_view(['GET','POST'])
def departmentList(request):
    if request.method == "GET":
        mydata = Department.objects.all()
        all_data = DepartmentSerializer(mydata,many=True)
        return JsonResponse(all_data.data,safe=False)

    elif request.method == "POST":
        mydata = JSONParser().parse(request)
        new_data = DepartmentSerializer(data=mydata)
        if new_data.is_valid():
            new_data.save()
            return JsonResponse(new_data.data,status = status.HTTP_201_CREATED)  
        return JsonResponse(new_data.error,status = status.HTTP_400_BAD_REQUEST)      


@api_view(['PUT','DELETE'])
def departmentModify(request,pk):
    data = Department.objects.get(id=pk)
    if request.method == "PUT":
        mydata = JSONParser().parse(request)
        new_data = DepartmentSerializer(data,data=mydata)
        if new_data.is_valid():
            new_data.save()
            return JsonResponse(new_data.data,status = status.HTTP_201_CREATED)  
        return JsonResponse(new_data.error,status = status.HTTP_400_BAD_REQUEST) 

    elif request.method == "DELETE":
        data.delete()
        return JsonResponse({'message':'deleted data'},status=status.HTTP_204_NO_CONTENT)

@api_view(["GET","POST"])
def employeeList(request):
    if request.method == "GET":
        data = Employee.objects.all()
        all_data = EmployeeSerializer(data,many=True)
        return JsonResponse(all_data.data,safe=False) 

    elif request.method == "POST":
        new_data = EmployeeSerializer(data=request.data,partial=True)
        if new_data.is_valid():
            new_data.save()
            return JsonResponse(new_data.data,status = status.HTTP_201_CREATED)


@api_view(['PUT','DELETE','PATCH'])
def employeeModify(request,pk):
    old_data = Employee.objects.get(id=pk)
    if request.method == "PUT":
        new_data = EmployeeSerializer(old_data,data=request.data,partial=True)
        if new_data.is_valid():
            new_data.save()
            return JsonResponse(new_data.data,status = status.HTTP_201_CREATED)     

    elif request.method == "DELETE":
        old_data.delete()
        return JsonResponse({'message':'deleted data'},status=status.HTTP_204_NO_CONTENT)               
          
    elif request.method == "PATCH":
        new_data = EmployeeSerializer(old_data,data=request.data,partial=True)
        if new_data.is_valid():
            new_data.save()
            return JsonResponse(new_data.data,status = status.HTTP_201_CREATED)


class DepartmentApi(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeApi(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @action(detail=True, methods=['POST'])
    def upload_image(request):
        try:
            file = request.data['file']
        except KeyError:
            raise ParseError('Request has no resource file attached')
        employee = Employee.objects.create(image=file)