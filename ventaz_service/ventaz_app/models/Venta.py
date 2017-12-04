from django.db import models
from .Cliente import Cliente
from .EstablecimientoNegocio import EstablecimientoNegocio
from .Ingreso import Ingreso


class Venta(models.Model):
    FACTURA = 'FACTURA'
    BOLETA = 'BOLETA'
    TIPOCOMPROBANTE = ((FACTURA, 'FACTURA'), (BOLETA, 'BOLETA'),)
    CUOTAS = 'CUOTAS'
    CONTADO = 'CONTADO'
    TIPOVENTA = ((CUOTAS, 'CUOTAS'), (CONTADO, 'CONTADO'),)
    ABIERTA = 'ABIERTA'  # Se la asigna consecutivo al momento de ser creada, y permanecerá "Abierta" hasta el 
                        #momento de registrar la cancelación total de su saldo "por pagar". Una factura abierta 
                        #puede ser anulada, es decir, mantendrá su consecutivo pero no se tendrá en cuenta para 
                        #los el registro de ingresos.
    ANULADA = 'ANULADA'  # Cuando se crea una factura abierta y por alguna razón la venta no se realiza, se 
                        #cancela, o simplemente la factura no va a ser usada para intercambio comercial. La ley no 
                        #permite que una factura que ya tiene un consecutivo (factura abierta) sea eliminada, para 
                        #esto se decide anular la factura, lo cual indica que ésta no tiene efecto alguno en la 
                        #contabilidad de la empresa pero sigue guardando el consecutivo numérico.
    CERRADA = 'CERRADA'  # Ha sido cancelada por el cliente en su totalidad, y no puede cambiar su estado.
                        #Simplemente representa la realización de una venta y la cancelación total de la deuda. 
                        #Generalmente una factura pasa de Abierta a Cerrada.
    ESTADO = ((CERRADA, 'CERRADA'), (ANULADA, 'ANULADA'), (ABIERTA, 'ABIERTA'),)
    cliente_fk = models.ForeignKey(Cliente, null=True, blank=True)
    establecimientonegocio_fk = models.ForeignKey(EstablecimientoNegocio, null=True, blank=True)
    ingresos_fk = models.ManyToManyField(Ingreso, related_name='ingreso_related', null=True, blank=True)

    tipo_venta = models.CharField(max_length=10, choices=TIPOVENTA, default=CONTADO)
    fecha_venta = models.DateField(auto_now_add=True, blank=True, null=True)
    tipocomprobante = models.CharField(max_length=10, choices=TIPOCOMPROBANTE, default=FACTURA)
    cantidad = models.IntegerField(default=0, blank=True)
    precio_venta = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=10, choices=ESTADO, default=CERRADA)
    #descuento = models.IntegerField(default=0, blank=True)

    def ingreso_def(self):  # este nombre va para admin y serializaer
        return ",".join([str(p) for p in self.ingresos_fk.all()])

    class Meta:
        ordering = ['estado']
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
    
    def __unicode__(self):
        return self.estado

    def __str__(self):
        return self.estado
    