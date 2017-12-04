from django.db import models


class Cliente(models.Model):
    DNI = 'DNI'
    RUC = 'RUC'
    TIPODOC = ((DNI, 'DNI'), (RUC, 'RUC'),)
    HOMBRE = 'Hombre'
    MUJER = 'Mujer'
    GENERO = ((HOMBRE, 'Hombre'), (MUJER, 'Mujer'),)
    # ESTADO = ((0, 'Denegado'), (1, 'Activo'),)
    #nombre_cliente = models.CharField(max_length=50, blank=True, null=True, verbose_name='Cliente')
    apellidos_cliente = models.CharField(max_length=50, blank=True, null=True)# Indicamos null=True si queremos dejar el campo en blanco
    nombre_cliente = models.CharField(max_length=50, blank=True, null=True)# Indicamos null=True si queremos dejar el campo en blanco
    direccion_cliente = models.CharField(max_length=50, blank=True, null=True)# Indicamos null=True si queremos dejar el campo en blanco
    telefono_cliente = models.CharField(max_length=9, blank=True, null=True)# Indicamos null=True si queremos dejar el campo en blanco
    tipodoc_cliente = models.CharField(max_length=10, choices=TIPODOC, default=DNI)# Indicamos null=True si queremos dejar el campo en blanco
    numdoc_cliente = models.IntegerField(blank=True, null=True)# Indicamos null=True si queremos dejar el campo en blanco
    email_cliente = models.EmailField(max_length=50, null=True)# Indicamos null=True si queremos dejar el campo en blanco
    genero_cliente = models.CharField(max_length=10, choices=GENERO, default=HOMBRE)
    fechasuscripcion_cliente = models.DateField(auto_now_add=True, blank=True, null=True)# Indicamos null=True si queremos dejar el campo en blanco
    #fechasuscripcion_cliente = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # estado_cliente = models.BooleanField(default=True)
    # estado_cliente = models.IntegerField(default=1, choices=ESTADO)
    # foto = models.ImageField(upload_to='foto')

    class Meta:
        ordering = ['nombre_cliente']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    # SIRVE TAMBIEN PARA ENVIAR ESTE ATRIBUTO EN ESPECIAL A OTRA TABLA
    # ES OPCIONAL LO DE ABAJO, SI NO SE PONE SE ENVIARA POR DEFECTO
    def __unicode__(self):  # Python 2 para no mostrar "nombre object"
        return self.nombre_cliente#NO ACEPTA DATE O DATETIME

    def __str__(self):  # Python 3 para no mostrar "nombre object"
        return self.nombre_cliente#NO ACEPTA DATE O DATETIME
    """
    Este es un Comentario
    """