from django.shortcuts import render
# Create your views here.
from ..templates.ClienteForm import ClienteForm
from ..models.Cliente import Cliente
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from ..serializers import ClienteSerializer
def cliente(request):
    form = ClienteForm(request.POST or None)  # campos obligatorios
    # print (dir(form)) para saber comandos en cmd
    if form.is_valid():
        form_data = form.cleaned_data
        aba = form_data.get("nombre_cliente")
        abb = form_data.get("apellidos_cliente")
        abc = form_data.get("direccion_cliente")
        abd = form_data.get("telefono_cliente")
        abe = form_data.get("tipodoc_cliente")
        abf = form_data.get("numdoc_cliente")
        abg = form_data.get("email_cliente")
        abh = form_data.get("genero_cliente")
        abi = form_data.get("fechasuscripcion_cliente")
        obj = Cliente.objects.create(nombre_cliente=aba, apellidos_cliente=abb, direccion_cliente=abc, telefono_cliente=abd,
                                     tipodoc_cliente=abe, numdoc_cliente=abf, email_cliente=abg, genero_cliente=abh, fechasuscripcion_cliente=abi)
    context = {
        "var_form": form,
    }
    return render(request, "ClienteTemplate.py", context)
# ViewSets define the view behavior.
class ClienteViewSet(viewsets.ModelViewSet):  # API REST que permite a los usuarios ser vistos o editados.
    queryset = Cliente.objects.all()
    # queryset = Cliente.objects.filter()
    serializer_class = ClienteSerializer