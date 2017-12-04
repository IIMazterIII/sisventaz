from django.shortcuts import render
from ..models.Ingreso import Ingreso
from ..models.EstablecimientoNegocio import EstablecimientoNegocio
from ..models.Cliente import Cliente
from ..models.Venta import Venta
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from ..serializers import VentaSerializer


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
