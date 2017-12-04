from django.db import models
from .EstablecimientoNegocio import EstablecimientoNegocio
from .Almacen import Almacen


class Trabajador(models.Model):

    HOMBRE = 'Hombre'
    MUJER = 'Mujer'
    GENERO = ((HOMBRE, 'Hombre'), (MUJER, 'Mujer'),)

    establecimientonegocios_fk = models.ManyToManyField(EstablecimientoNegocio, related_name='establecimientonegocio_related', null=True, blank=True)
    def establecimientonegocio_def(self):  # este nombre va para admin y serializaer
        return ",".join([str(p) for p in self.establecimientonegocios_fk.all()])


    almacens_fk = models.ManyToManyField(Almacen, related_name='almacen_related', null=True, blank=True)
    def almacen_def(self):  # este nombre va para admin y serializaer
        return ",".join([str(p) for p in self.almacens_fk.all()])


    # apellidos_trabajador = ((0, 'Denegado'), (1, 'Activo'),)
    #nombre_trabajador = models.CharField(max_length=50, blank=True, null=True, verbose_name='Titulo')
    apellidos_trabajador = models.CharField(max_length=50, blank=True, null=True)
    nombre_trabajador = models.CharField(max_length=50, blank=True, null=True)
    direccion_trabajador = models.CharField(max_length=50, blank=True, null=True)
    telefono_trabajador = models.CharField(max_length=9, blank=True, null=True)
    numdoc_trabajador = models.IntegerField(blank=True, null=True)
    email_trabajador = models.EmailField(max_length=50, null=True)
    genero_trabajador = models.CharField(max_length=10, choices=GENERO, default=HOMBRE)

    class Meta:
        ordering = ['apellidos_trabajador']
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadors'

    def __unicode__(self):  # Python 2 para no mostrar "nombre object"
        return self.apellidos_trabajador

    def __str__(self):  # Python 3 para no mostrar "nombre object"
        return self.apellidos_trabajador
