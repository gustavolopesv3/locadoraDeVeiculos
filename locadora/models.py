from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField(max_length=11)
    data_nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.IntegerField(max_length=15)
    bairro = models.CharField(max_length=50)
    rua = models.CharField(max_length=50)
    numero = models.IntegerField(max_length=6)
    cep = models.IntegerField(max_length=10)

class Veiculo(models.Model):
    marca = models.ForeignKey('Marcas',on_delete=models.CASCADE)
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE)
    placa = models.CharField(max_length=10)
    chassi = models.CharField(max_length=20)
    cor = models.CharField(max_length=15)
    ano = models.IntegerField(max_length=5)

class Marcas(models.Model):
    nome = models.CharField(max_length=10)

class Modelo(models.Model):
    nome = models.CharField(max_length=10)


