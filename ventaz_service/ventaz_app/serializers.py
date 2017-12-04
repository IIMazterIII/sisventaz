from rest_framework import serializers, viewsets, routers
from django.conf.urls import url, include
from .models.Almacen import Almacen
from .models.Categoria import Categoria
from .models.Cliente import Cliente
from .models.EstablecimientoNegocio import EstablecimientoNegocio
from .models.Ingreso import Ingreso
from .models.Producto import Producto
from .models.Proveedor import Proveedor
from .models.Trabajador import Trabajador
from .models.Venta import Venta
# from django.contrib.auth.models import User, Group
# Serializers define the API representation.
# Aquí será donde representemos los datos que queremos devolver a través de la api


class AlmacenSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Almacen
        fields = ('id', 'nombre_almacen', 'direccion_almacen', 'telefono_almacen')


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Categoria
        fields = ('id', 'nombre_categoria', 'descripcion_categoria')


class ClienteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cliente
        # fields = ('url','id', 'nombre_cliente')
        fields = ('id', 'nombre_cliente', 'apellidos_cliente', 'direccion_cliente', 'telefono_cliente',
                  'tipodoc_cliente', 'numdoc_cliente', 'email_cliente', 'genero_cliente', 'fechasuscripcion_cliente')


class EstablecimientoNegocioSerializer(serializers.ModelSerializer):

    class Meta:
        model = EstablecimientoNegocio
        fields = ('id', 'nombre_en', "direccion_en", "telefono_en")


class IngresoSerializer(serializers.ModelSerializer):
    # PARA MANDAR OTROS PARAMETROS DISTINTO AL ID
    almacen_str = serializers.ReadOnlyField(
        source='almacen_fk.nombre_almacen')  # envia string para listar

    proveedor_str = serializers.ReadOnlyField(
        source='proveedor_fk.razon_social')  # envia string para listar

    producto_id = serializers.ReadOnlyField(
        source='productos_fk.nombre_producto')  # envia ID para CRUD

    producto_str = serializers.ReadOnlyField(
        source='producto_def.nombre_producto')  # envia string para listar

    class Meta:
        model = Ingreso
        fields = ('id', 'almacen_str', 'almacen_fk',
                  'proveedor_str', 'proveedor_fk',
                  'producto_id', 'productos_fk',
                  'producto_str', 'producto_def',
                  'fecha_ingreso', 'fecha_vencimiento', 'tipocomprobante', 'precio_compra',
                  'stock_inicial', 'stock_actual', 'estado', 'producto_str')


class ProductoSerializer(serializers.ModelSerializer):
    # PARA MANDAR OTROS PARAMETROS DISTINTO AL ID
    categoria_str = serializers.ReadOnlyField(
        source='categoria_fk.nombre_categoria')  # envia string para listar

    class Meta:
        model = Producto
        fields = ('id', 'categoria_str', 'categoria_fk',
                  'nombre_producto', 'unidad_medida', 'descripcion_producto')


class ProveedorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Proveedor
        fields = ('id', 'razon_social', 'direccion_proveedor', 'telefono_proveedor',
                  'tipodoc_proveedor', 'numdoc_proveedor', 'email_proveedor')


class TrabajadorSerializer(serializers.HyperlinkedModelSerializer):
    # PARA MANDAR OTROS PARAMETROS DISTINTO AL ID
    establecimientonegocio_id = serializers.ReadOnlyField(
        source='establecimientonegocios_fk.nombre_en')  # envia ID para CRUD

    establecimientonegocio_str = serializers.ReadOnlyField(
        source='establecimientonegocio_def.nombre_en')  # envia string para listar

    almacen_id = serializers.ReadOnlyField(
        source='almacens_fk.nombre_almacen')  # envia ID para CRUD

    almacen_str = serializers.ReadOnlyField(
        source='almacen_def.nombre_almacen')  # envia string para listar

    class Meta:
        model = Trabajador
        fields = ('id', 'establecimientonegocio_id', 'establecimientonegocios_fk',
                  'establecimientonegocio_str', 'establecimientonegocio_def',
                  'almacen_id', 'almacens_fk',
                  'almacen_str', 'almacen_def',
                  'apellidos_trabajador', 'nombre_trabajador',
                  'direccion_trabajador', 'telefono_trabajador',
                  'tipodoc_trabajador', 'numdoc_trabajador',
                  'email_trabajador', 'genero_trabajador')


class VentaSerializer(serializers.ModelSerializer):
    # PARA MANDAR OTROS PARAMETROS DISTINTO AL ID
    cliente_str = serializers.ReadOnlyField(
        source='cliente_fk.apellidos_cliente')  # envia string para listar

    establecimientonegocio_str = serializers.ReadOnlyField(
        source='establecimientonegocio_fk.establecimientonegocio')  # envia string para listar

    ingreso_id = serializers.ReadOnlyField(
        source='ingresos_fk.fecha_ingreso')  # envia ID para CRUD

    ingreso_str = serializers.ReadOnlyField(
        source='ingreso_def.fecha_ingreso')  # envia string para listar

    class Meta:
        model = Venta
        fields = ('id', 'cliente_str', 'cliente_fk',
                  'establecimientonegocio_str', 'establecimientonegocio_fk',
                  'ingreso_id','ingresos_fk',
                  'ingreso_str','ingreso_def',
                  'tipo_venta', 'fecha_venta', 'tipocomprobante', 'cantidas', 'precio_venta', 'estado')

