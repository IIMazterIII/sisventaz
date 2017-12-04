from django.db import models
from .Categoria import Categoria

class Producto(models.Model):
    #on_delete=models.CASCADE
    categoria_fk = models.ForeignKey(Categoria, null=True, blank=True)

    nombre_producto = models.CharField(max_length=50, blank=True, null=True)
    unidad_medida = models.CharField(max_length=50, blank=True, null=True)
    descripcion_producto = models.TextField(max_length=350, blank=True, null=True)

    class Meta:
        ordering = ['nombre_producto']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    def __unicode__(self):  # Python 2 para no mostrar "nombre object"
        return self.nombre_producto
    def __str__(self):  # Python 3 para no mostrar "nombre object"
        return self.nombre_producto
