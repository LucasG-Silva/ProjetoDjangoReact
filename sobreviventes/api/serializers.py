from rest_framework import serializers
from sobreviventes import models

class SobreviventesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.sobreviventes
        fields = '__all__'