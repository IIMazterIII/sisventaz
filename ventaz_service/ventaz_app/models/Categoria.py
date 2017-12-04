from django.db import models


class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50, blank=True, null=True)
    descripcion_categoria = models.TextField(max_length=350, blank=True, null=True)

    class Meta:
        ordering = ['nombre_categoria']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __unicode__(self):
        return self.nombre_categoria

    def __str__(self):
        return self.nombre_categoria
