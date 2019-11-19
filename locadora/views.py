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
def editarveiculo(request, id):
    veiculo_ant = Veiculo.objects.get(id=id)
    form = FormVeiculo(request.POST or None, instance=veiculo_ant)

    if form.is_valid():
        form = form.save()
        form.save()
        return redirect('/')
    return render(request, 'editarveiculo.html', {'form': form, })

@login_required()
def receberalguel(request, id):
    alugado = Alguel.objects.get(id=id)
    form = FormAluguel(request.POST or None, instance=alugado)
    if form.is_valid():
        alguelform = form.save()
        alguelform.save()
        return redirect('listaraluguel')
    return render(request, 'receberlocacao.html', {'form': form})

@login_required()
def deletarveiculo(request, id):
    veiculo_delete = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo_delete.delete()
        return redirect('listarveiculos')
    return render(request, 'veiculo-confirma-delete.html', {'veiculo_delete': veiculo_delete, })


@login_required()
def cadastromarca(request):
    if request.method == 'POST':
        form = FormMarca(request.POST)
        if form.is_valid():
            marcaform = form.save()
            marcaform.save()
            return redirect('/')
    form = FormMarca()
    return render(request, 'cadastromarca.html', {'form': form})

@login_required()
def cadastromodelo(request):

    if request.method == 'POST':
        form = FormModelo(request.POST)
        if form.is_valid():
            modeloform = form.save()
            modeloform.save()
            return redirect('/')
    form = FormModelo()
    return render(request, 'cadastromodelo.html', {'form': form})


@login_required()
def alguel(request):
    if request.method == 'POST':
        form = FormAluguel(request.POST)
        if form.is_valid():
            alguelform = form.save()
            alguelform.save()
            return redirect('/')
    form = FormAluguel()
    return render(request, 'aluguel.html', {'form': form})




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
    locacoes = Alguel.objects.all().count()
    return render(request, 'base.html', locals())

@login_required()
def login(request):
    if request.method =='POST':
        user = authenticate(username=request.POST['usarname'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/equipamentos')
    return render(request, 'registration/login.html')

@login_required()
def listaralguel(request):
    listaluguel = Alguel.objects.filter(data_recebimento__isnull=True)
    return render(request, 'listaraluguel.html', locals())
@login_required()
def listaralguel_finalizado(request):
    listaluguel = Alguel.objects.filter(data_recebimento__isnull=False)
    return render(request, 'locacoes_finalizadas.html', locals())


@login_required()
def listarveiculos(request):
    listaveiculo = Veiculo.objects.filter(status='DISPONIVEL')
    return render(request, 'listarveiculos.html', locals())

def teste(request):
    return render(request, 'teste.html')