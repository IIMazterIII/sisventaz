from django.shortcuts import render
from ..models.EstablecimientoNegocio import EstablecimientoNegocio
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from ..serializers import EstablecimientoNegocioSerializer


class EstablecimientoNegocioViewSet(viewsets.ModelViewSet):
    queryset = EstablecimientoNegocio.objects.all()
    serializer_class = EstablecimientoNegocioSerializer
