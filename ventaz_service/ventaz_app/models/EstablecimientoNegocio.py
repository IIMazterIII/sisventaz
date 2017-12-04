from django.db import models


class EstablecimientoNegocio(models.Model):
    nombre_en = models.CharField(max_length=50, blank=True, null=True)
    direccion_en = models.CharField(max_length=50, blank=True, null=True)
    telefono_en = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        ordering = ['nombre_en']
        verbose_name = 'EstablecimientoNegocio'
        verbose_name_plural = 'EstablecimientoNegocios'

    def __unicode__(self):
        return self.nombre_en

    def __str__(self):
        return self.nombre_en
