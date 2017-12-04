from django.shortcuts import render
# Create your views here.
from ..models.Almacen import Almacen
from ..models.EstablecimientoNegocio import EstablecimientoNegocio
from ..models.Trabajador import Trabajador

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from ..serializers import TrabajadorSerializer

# ViewSets define the view behavior.
class TrabajadorViewSet(viewsets.ModelViewSet):  # API REST que permite a los usuarios ser vistos o editados.
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer