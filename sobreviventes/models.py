from email.policy import default
from pyexpat import model
from django.db import models
from uuid import uuid4

# Create your models here.

class sobreviventes(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid4, editable = False)
    nome = models.CharField(max_length = 100)
    usuario = models.CharField(max_length = 50)
    idade = models.IntegerField()
    sexo = models.CharField(max_length = 9)
    latitude = models.FloatField()
    longitude = models.FloatField()