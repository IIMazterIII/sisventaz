# -*- coding: utf-8 -*-
from django.conf.urls import *
from django.conf.urls import include, url
#from django.conf import settings
from rest_framework import routers

from .views import ClienteView
#from .views import ClienteViewSet
from .views.AlmacenView import AlmacenViewSet
from .views.CategoriaView import CategoriaViewSet
from .views.ClienteView import ClienteViewSet
from .views.EstablecimientoNegocioView import EstablecimientoNegocioViewSet
from .views.IngresoView import IngresoViewSet
from .views.ProductoView import ProductoViewSet
from .views.ProveedorView import ProveedorViewSet
from .views.TrabajadorView import TrabajadorViewSet
from .views.VentaView import VentaViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'almacens', AlmacenViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'sstablecimientonegocios', EstablecimientoNegocioViewSet)
router.register(r'ingresos', IngresoViewSet)
router.register(r'prodcutos', ProductoViewSet)
router.register(r'proveedors', ProveedorViewSet)
router.register(r'trabajadors', TrabajadorViewSet)
router.register(r'ventas', VentaViewSet)
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
# urlpatterns = patterns(
#'',
#url(r'^', include(router.urls)),
#)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^api-token-auth/', include('rest_framework.authtoken.views.obtain_auth_token')),
]