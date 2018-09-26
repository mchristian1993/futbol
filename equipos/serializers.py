from rest_framework import serializers
from .models import Equipos

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipos
        fields = ('id', 'nombre_equipo', 'liga','tecnico')