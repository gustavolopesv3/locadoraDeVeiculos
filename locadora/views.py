from django.shortcuts import render

from locadora.forms import *


def cadastrocliente(request):
    formcliente = FormCliente
    return render(request, 'index.html',locals())

def cadastroveiculo(request):
    formveiculo = FormVeiculo
    return render(request, 'cadastroveiculo.html', locals())

