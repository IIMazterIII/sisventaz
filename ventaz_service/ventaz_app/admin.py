from django.contrib import admin
# Register your models here.
from .models.Almacen import Almacen
from .models.Categoria import Categoria
from .models.Cliente import Cliente
from .models.EstablecimientoNegocio import EstablecimientoNegocio
from .models.Ingreso import Ingreso
from .models.Producto import Producto
from .models.Proveedor import Proveedor
from .models.Trabajador import Trabajador
from .models.Venta import Venta


class AlmacenAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["nombre_almacen", "direccion_almacen", "telefono_almacen"]
    list_display_links = ["nombre_almacen"]
    list_editable = ["telefono_almacen"]
    search_fields = ["nombre_almacen"]


class CategoriaAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["nombre_categoria","descripcion_categoria"]
    list_display_links = ["nombre_categoria"]
    list_editable = ["descripcion_categoria"]
    search_fields = ["nombre_categoria"]


class ClienteAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["apellidos_cliente", "nombre_cliente", "direccion_cliente", "telefono_cliente",
                    "tipodoc_cliente", "numdoc_cliente", "email_cliente", "genero_cliente", "fechasuscripcion_cliente"]
    list_display_links = ["apellidos_cliente", "nombre_cliente"]
    list_editable = ["direccion_cliente", "telefono_cliente", "email_cliente"]
    search_fields = ["nombre_cliente", "apellidos_cliente", "numdoc_cliente"]
    # form = PacienteModelForm       # OPCIONAL para ModelForm
    # class Meta: HABILITAR EN MODO NORMAL SIN MODELFORM
    # model = Cliente  HABILITAR EN MODO NORMAL SIN MODELFORM


class EstablecimientoNegocioAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["nombre_en", "direccion_en", "telefono_en"]
    list_display_links = ["nombre_en"]
    list_editable = ["telefono_en"]
    search_fields = ["nombre_en"]


class IngresoAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["almacen_fk", "proveedor_fk", "producto_fk", "producto_str","fecha_ingreso",
                    "fecha_vencimiento", "tipocomprobante", "precio_compra", "stock_inicial",
                    "stock_actual", "estado"]
    #list_display_links = ["almacen_fk"]
    #list_editable = ["tipocomprobante"]
    #search_fields = ["almacen_fk", "fecha_ingreso"]


class ProductoAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["categoria_fk", "nombre_producto", "unidad_medida", "descripcion_producto"]
    list_display_links = ["categoria_fk"]
    list_editable = ["descripcion_producto", "unidad_medida"]
    search_fields = ["nombre_producto"]


class ProveedorAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["razon_social", "direccion_proveedor", "telefono_proveedor",
                    "tipodoc_proveedor", "numdoc_proveedor", "email_proveedor"]
    list_display_links = ["razon_social"]
    list_editable = ["direccion_proveedor", "telefono_proveedor"]
    search_fields = ["razon_social"]


class TrabajadorAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["apellidos_trabajador", "nombre_trabajador", "almacen_def", "establecimientonegocio_def",
                    "direccion_trabajador", "telefono_trabajador", "numdoc_trabajador", "email_trabajador",
                    "genero_trabajador"]
    #list_display_links = ["apellidos_trabajador"]
    #list_editable = ["telefono_trabajador", "direccion_trabajador"]
    #search_fields = ["apellidos_trabajador"]


class VentaAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["cliente_fk", "establecimientonegocio_fk", "ingreso_def", "tipo_venta", "fecha_venta",
                    "tipocomprobante", "cantidad", "precio_venta", "estado"]
                    #ingreso_def
    search_fields = ["cliente_fk", "establecimientonegocio_fk", "estado"]

    #fields = ['biblioteca',('editorial', 'genero', 'edicion'), ('nombre', 'fecha_publicacion')]
    #readonly_fields = ('biblioteca',)
    #filter_horizontal= ('autores',)

admin.site.register(Almacen, AlmacenAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(EstablecimientoNegocio, EstablecimientoNegocioAdmin)
admin.site.register(Ingreso, IngresoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Trabajador, TrabajadorAdmin)
admin.site.register(Venta, VentaAdmin)
