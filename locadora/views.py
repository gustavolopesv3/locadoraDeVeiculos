from django.shortcuts import render, redirect

from locadora.forms import *


def cadastrocliente(request):
    if request.method == 'POST':
        form = FormCliente(request.POST)
        if form.is_valid():
            marcaform = form.save()
            marcaform.save()
            return redirect('/')
    form = FormCliente()
    return render(request, 'index.html', {'form': form})



def cadastroveiculo(request):
    formveiculo = FormVeiculo
    return render(request, 'cadastroveiculo.html', locals())

def alguel(request):
    formaluguel = FormAluguel
    return render(request, 'aluguel.html', locals())

def base(request):
    return render(request, 'base.html')

def listclientes(request):
    cliente = Cliente.objects.all()
    return render(request, 'listclientes.html', locals())