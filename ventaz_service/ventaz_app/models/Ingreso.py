from django.db import models
from .Almacen import Almacen
from .Proveedor import Proveedor
from .Producto import Producto


class Ingreso(models.Model):
    FACTURA = 'FACTURA'
    BOLETA = 'BOLETA'
    TIPOCOMPROBANTE = ((FACTURA, 'FACTURA'), (BOLETA, 'BOLETA'),)
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
    almacen_fk = models.ForeignKey(Almacen, null=True, blank=True)
    proveedor_fk = models.ForeignKey(Proveedor, null=True, blank=True)
    producto_fk = models.ForeignKey(Producto, related_name='producto_related', null=True, blank=True)
    producto_str = models.CharField(max_length=50, blank=True, null=True)

    fecha_ingreso = models.DateField(auto_now_add=True, blank=True, null=True)
    fecha_vencimiento = models.DateField(auto_now_add=True, blank=True, null=True)
    tipocomprobante = models.CharField(max_length=10, choices=TIPOCOMPROBANTE, default=FACTURA)
    precio_compra = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    stock_inicial = models.IntegerField(default=0, blank=True)
    stock_actual = models.IntegerField(default=0, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADO, default=CERRADA)

    class Meta:
        ordering = ['fecha_ingreso']
        verbose_name = 'Ingreso'
        verbose_name_plural = 'Ingresos'
    
    def __unicode__(self):
        return self.producto_str

    def __str__(self):
        return self.producto_str
    
    