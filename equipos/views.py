from rest_framework import generics
from .serializers import SongsSerializer
from .models import Equipos

class EquiposList(generics.ListAPIView):
    queryset = Equipos.objects.all()
    serializer_class = SongsSerializer