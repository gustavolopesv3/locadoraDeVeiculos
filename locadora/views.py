from django.shortcuts import render, redirect

from locadora.forms import *


def cadastrocliente(request):
    if request.method == 'POST':
        form = FormCliente(request.POST)
        if form.is_valid():
            clienteform = form.save()
            clienteform.save()
            return redirect('/')
    form = FormCliente()
    return render(request, 'cadastrocliente.html', {'form': form})



def cadastroveiculo(request):
    if request.method == 'POST':
        form = FormVeiculo(request.POST)
        if form.is_valid():
            veiculoform = form.save()
            veiculoform.save()
            return redirect('/')
    form = FormVeiculo()
    return render(request, 'cadastroveiculo.html', {'form': form})

def cadastromarca(request):
    if request.method == 'POST':
        form = FormMarca(request.POST)
        if form.is_valid():
            marcaform = form.save()
            marcaform.save()
            return redirect('/')
    form = FormMarca()
    return render(request, 'cadastromarca.html  ', {'form': form})

def cadastromodelo(request):
    if request.method == 'POST':
        form = FormModelo(request.POST)
        if form.is_valid():
            modeloform = form.save()
            modeloform.save()
            return redirect('/')
    form = FormMarca()
    return render(request, 'cadastromodelo.html', {'form': form})



def alguel(request):
    formaluguel = FormAluguel
    return render(request, 'aluguel.html', locals())

def base(request):
    return render(request, 'base.html')

def listclientes(request):
    cliente = Cliente.objects.all()
    return render(request, 'listclientes.html', locals())