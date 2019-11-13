from django import forms
from locadora.models import *


class FormCliente(forms.ModelForm):
    cpf = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control cpf-inputmask', 'id': 'cpfcnpj',}
        ),
    )
    data_nascimento = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control dataNascimento-inputmask', 'type': 'date',}
        ),
    )
    cep = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control dataNascimento-inputmask', 'id': 'cep',}
        ),
    )

    telefone = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control telefone-inputmask', 'id': 'telefone',}
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
    data_retorno = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control dataNascimento-inputmask', 'id': 'dataNascimento', }
        ),
    )
    valor = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control salario-inputmask', 'id': 'valor', }
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

