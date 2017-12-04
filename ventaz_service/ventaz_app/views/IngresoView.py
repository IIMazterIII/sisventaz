from django.shortcuts import render
from ..models.Almacen import Almacen
from ..models.Proveedor import Proveedor
from ..models.Producto import Producto
from ..models.Ingreso import Ingreso
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from ..serializers import IngresoSerializer


class IngresoViewSet(viewsets.ModelViewSet):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer
