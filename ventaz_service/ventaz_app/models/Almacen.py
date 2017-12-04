from django.db import models


class Almacen(models.Model):
    nombre_almacen = models.CharField(max_length=50, blank=True, null=True)
    direccion_almacen = models.CharField(max_length=50, blank=True, null=True)
    telefono_almacen = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        ordering = ['nombre_almacen']
        verbose_name = 'Almacen'
        verbose_name_plural = 'Almacens'

    def __unicode__(self):
        return self.nombre_almacen

    def __str__(self):
        return self.nombre_almacen
