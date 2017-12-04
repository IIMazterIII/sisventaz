from django import forms
from ..models.Cliente import Cliente
import datetime
TIPODOC = (
    ('DNI', 'DNI'),
    ('RUC', 'RUC'),
)
GENERO = (
    ('Hombre', 'Hombre'),
    ('Mujer', 'Mujer'),
)
class ClienteForm(forms.Form):
    apellidos_cliente = forms.CharField(max_length=50)
    nombre_cliente = forms.CharField(max_length=50)
    direccion_cliente = forms.CharField(max_length=50)
    telefono_cliente = forms.CharField(max_length=9)
    tipodoc_cliente = forms.CharField(max_length=10, widget=forms.Select(choices=TIPODOC))
    numdoc_cliente = forms.IntegerField()
    email_cliente = forms.EmailField(max_length=50, help_text='example@example.com')
    genero_cliente = forms.CharField(max_length=10, widget=forms.Select(choices=GENERO))
    fechasuscripcion_cliente = forms.DateField(initial=datetime.date.today, help_text='A/M/D')#PARA FECHA
    #fechasuscripcion_cliente = forms.DateTimeField(initial=datetime.datetime.today, help_text='A/M/D H:M:S')#PARA FECHA Y HORA
