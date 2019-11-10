from django import forms
from locadora.models import *


class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class FormVeiculo(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'

class FormAluguel(forms.ModelForm):
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

