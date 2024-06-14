from enum import Enum
from django.db import models
from django.core.validators import MinLengthValidator


class Role(Enum):
    ADMIN = 'Admin'


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, null=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(validators=[MinLengthValidator(8)], max_length=20, blank=False, null=False, unique=True)
    role = models.CharField(max_length=20, choices=[(role.value, role.name) for role in Role]) 


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=200, null=False)
    date = models.DateField()