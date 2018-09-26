from django.urls import path
from .views import EquiposList

urlpatterns = [
    path('equipos/', EquiposList.as_view(), name="equipos-all")
]