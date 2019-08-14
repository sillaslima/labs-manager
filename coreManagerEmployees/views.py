from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from coreManagerEmployees.models import Employee,Departament
from .serializers import DepartamentSerializer, EmployeeSerializer

class DepartamentsViewSet ( generics.ListAPIView ):
    queryset = Departament.objects.all()
    serializer_class = DepartamentSerializer
    name='departament-list'


class EmployeeViewSet (generics.ListAPIView):
     queryset = Employee.objects.all()
     serializer_class = EmployeeSerializer
     name='employee-list'

class EmployeeDeleteViewSet ( generics.DestroyAPIView ):
    queryset = Employee.objects.all ( )
    serializer_class = EmployeeSerializer
    name = 'employee-delete'


class EmployeeCreateViewSet ( generics.CreateAPIView ):
    queryset = Employee.objects.all ( )
    serializer_class = EmployeeSerializer
    name='employee-create'


class EmployeeUpdateViewSet ( generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all ( )
    serializer_class = EmployeeSerializer
    name='employee-update'

class EmployeeDetailViewSet ( generics.RetrieveAPIView):
    queryset = Employee.objects.all ( )
    serializer_class = EmployeeSerializer
    name='employee-detail'




class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({

            'employee-list': reverse(EmployeeViewSet.name, request=request),
            })