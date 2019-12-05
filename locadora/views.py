from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
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
def editarcliente(request, id):
    cleinte_ant = Cliente.objects.get(id=id)
    form = FormCliente(request.POST or None, instance=cleinte_ant)
    if form.is_valid():
        clienteform = form.save()
        clienteform.save()
        return redirect('/')
    return render(request, 'cadastrocliente.html', {'form': form})

@login_required()
def listaveic_cliente(request, id):
    carros_cliente = Alguel.objects.filter(cliente=id)
    return render(request, 'carros_cliente.html', locals())



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
    form = FormReceberAluguel(request.POST or None, instance=alugado)
    if form.is_valid():
        alguelform = form.save()
        alguelform.save()
        carro = Veiculo.objects.get(id=int(request.POST.get('veiculo')))
        carro.status = 'DISPONIVEL'
        carro.save()
        return redirect('listaraluguel_finalizado')
    return render(request, 'receberlocacao.html', {'form': form})

@login_required()
def deletarveiculo(request, id ):
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
            carro = Veiculo.objects.get(id=int(request.POST.get('veiculo')))
            print(carro)
            carro.status = 'INDISPONIVEL'
            carro.save()
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
    locacoes = Alguel.objects.filter(data_recebimento='').count()
    locacoesfim = Alguel.objects.filter(data_recebimento__isnull=False).count()
    veiculosdisponivel = Veiculo.objects.filter(status='DISPONIVEL').count()
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
    listaluguel = Alguel.objects.filter(data_recebimento='')
    return render(request, 'listaraluguel.html', locals())



@login_required()
def listaralguel_finalizado(request):
    listaluguel = Alguel.objects.filter(data_recebimento__gt=0)
    return render(request, 'locacoes_finalizadas.html', locals())


@login_required()
def listarveiculos(request):
    listaveiculo = Veiculo.objects.filter(status='DISPONIVEL')
    return render(request, 'listarveiculos.html', locals())
@login_required
def todos_carros(request):
    carros = Veiculo.objects.all()
    return render(request, 'todos_veiculos.html', locals())

@login_required()
def cadastrar_usuario(request):
    if request.method == 'POST':
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('index')
    else:
        form_usuario = UserCreationForm()
    return render(request,'registration/cadastro_usuario.html', {'form_usuario': form_usuario})

def listar_ususario(request):
    user = UserCreationForm.username

    return render(request, 'listar_usuarios.html', locals())

def teste(request):
    return render(request, 'teste.html')