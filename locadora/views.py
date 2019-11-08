from django.shortcuts import render

from locadora.forms import *


def cadastrocliente(request):
    formcliente = FormCliente
    return render(request, 'index.html',locals())

def cadastroveiculo(request):
    formveiculo = FormVeiculo
    return render(request, 'cadastroveiculo.html', locals())

def alguel(request):
    formaluguel = FormAluguel
    return render(request, 'aluguel.html', locals())

def base(request):
    return render(request, 'base.html')


