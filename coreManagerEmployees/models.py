from django.db import models


# Create your models here.

class Departament(models.Model):
    name = models.CharField(max_length=49, blank=False, null=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=156, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False, unique=True)
    departament = models.ForeignKey(Departament, on_delete=False, blank=True, null=True, default='TBD')

    def __str__(self):
        return self.name
