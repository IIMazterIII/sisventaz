from django.shortcuts import render

# Create your views here.
from ..models.Categoria import Categoria
from ..models.Producto import Producto

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from ..serializers import ProductoSerializer

# ViewSets define the view behavior.


# API REST que permite a los usuarios ser vistos o editados.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    # queryset = Cuentausuario.objects.filter()
    serializer_class = ProductoSerializer
