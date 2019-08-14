from rest_framework import serializers
from .models import Departament, Employee


class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = ('id','name')



class EmployeeSerializer(serializers.ModelSerializer):
    departament = serializers.SlugRelatedField ( queryset=Departament.objects.all ( ) , slug_field='name' )

    class Meta:
        model = Employee
        fields = ('id', 'name', 'email', 'departament')
