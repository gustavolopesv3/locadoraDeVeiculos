from django.shortcuts import render

from locadora.forms import FormCliente


def cadastrocliente(request):
    formcliente = FormCliente
    return render(request, 'index.html',locals())

