from pyexpat import model
from rest_framework import viewsets
from sobreviventes.api import serializers
from sobreviventes import models

class SobreviventesViewSet(viewsets.ModelViewSet):
    serializer_class =  serializers.SobreviventesSerializer
    queryset = models.sobreviventes.objects.all()