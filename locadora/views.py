from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from locadora.forms import *

@login_required()
def cadastrocliente(request):
    if request.method == 'POST':
        form = FormCliente(request.POST)
        if form.is_valid():
            clienteform = form.save()
            clienteform.save()
            return redirect('/')
    form = FormCliente()
    return render(request, 'cadastrocliente.html', {'form': form})


@login_required()
def cadastroveiculo(request):
    if request.method == 'POST':
        form = FormVeiculo(request.POST)
        if form.is_valid():
            veiculoform = form.save()
            veiculoform.save()
            return redirect('/')
    form = FormVeiculo()
    return render(request, 'cadastroveiculo.html', {'form': form})

@login_required()
def cadastromarca(request):
    if request.method == 'POST':
        form = FormMarca(request.POST)
        if form.is_valid():
            marcaform = form.save()
            marcaform.save()
            return redirect('/')
    form = FormMarca()
    return render(request, 'cadastromarca.html  ', {'form': form})

@login_required()
def cadastromodelo(request):
    if request.method == 'POST':
        form = FormModelo(request.POST)
        if form.is_valid():
            modeloform = form.save()
            modeloform.save()
            return redirect('/')
    form = FormMarca()
    return render(request, 'cadastromodelo.html', {'form': form})


@login_required()
def alguel(request):
    formaluguel = FormAluguel
    return render(request, 'aluguel.html', locals())

@login_required()
def base(request):
    return render(request, 'base.html')

@login_required()
def listclientes(request):
    cliente = Cliente.objects.all()
    return render(request, 'listclientes.html', locals())

@login_required()
def contaclientes(request):
    contclientes = Cliente.objects.all().count()
    return render(request, 'base.html', locals())

@login_required()
def login(request):
    if request.method =='POST':
        user = authenticate(username=request.POST['usarname'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/equipamentos')
    return render(request, 'registration/login.html')