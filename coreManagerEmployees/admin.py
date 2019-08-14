from django.contrib import admin

# Register your models here.
from coreManagerEmployees.models import Employee, Departament
admin.site.register(Employee)
admin.site.register(Departament)