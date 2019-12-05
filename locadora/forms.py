from django import forms
from locadora.models import *


class FormCliente(forms.ModelForm):
    cpf = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control cpfcnpj-inputmask', 'id': 'cpf',}
        ),
    )
    data_nascimento = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control dataNascimento-inputmask', 'id': 'dataNascimento',}
        ),
    )
    telefone = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control telefone-inputmask', 'id': 'celular',}
        ),
    )
    cep = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control ', 'id': 'cep',}
        ),
    )



    class Meta:
        model = Cliente
        fields = '__all__'

class FormVeiculo(forms.ModelForm):
    placa = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control placa-inputmask', 'id': 'placa',}
        ),
    )

    class Meta:
        model = Veiculo
        fields = '__all__'


class FormAluguel(forms.ModelForm):
    veiculo = forms.ModelChoiceField(
        queryset=Veiculo.objects.exclude(status='INDISPONIVEL'),
        label='', empty_label="Selecione o veiculo",
        widget=forms.Select(attrs={'class': 'form-control w-100'}))



    data_retorno = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control dataNascimento-inputmask', 'id': 'dataNascimento', }
        ),
    )


    data_recebimento = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'dataNascimento', }
        ),
    )



    valor = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control salario-inputmask', 'id': 'salario', }
        ),
    )

    class Meta:
        model = Alguel
        fields = '__all__'

class FormReceberAluguel(forms.ModelForm):
    veiculo = forms.ModelChoiceField(
        queryset=Veiculo.objects.exclude(status='DISPONIVEL'),
        label='', empty_label="Selecione o veiculo",
        widget=forms.Select(attrs={'class': 'form-control w-100'}))



    data_retorno = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control dataNascimento-inputmask', 'id': 'dataNascimento', }
        ),
    )


    data_recebimento = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'dataNascimento', }
        ),
    )



    valor = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control salario-inputmask', 'id': 'salario', }
        ),
    )

    class Meta:
        model = Alguel
        fields = '__all__'

class FormMarca(forms.ModelForm):
    class Meta:
        model = Marcas
        fields = '__all__'

class FormModelo(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = '__all__'

