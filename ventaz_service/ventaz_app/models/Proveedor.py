from django.db import models


class Proveedor(models.Model):
    DNI = 'DNI'
    RUC = 'RUC'
    TIPODOC = ((DNI, 'DNI'), (RUC, 'RUC'),)
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    direccion_proveedor = models.CharField(max_length=50, blank=True, null=True)
    telefono_proveedor = models.CharField(max_length=9, blank=True, null=True)
    tipodoc_proveedor = models.CharField(max_length=10, choices=TIPODOC, default=DNI)
    numdoc_proveedor = models.IntegerField(blank=True, null=True)
    email_proveedor = models.EmailField(max_length=50, null=True)

    class Meta:
        ordering = ['razon_social']
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedors'

    def __unicode__(self):
        return self.razon_social

    def __str__(self):
        return self.razon_social
