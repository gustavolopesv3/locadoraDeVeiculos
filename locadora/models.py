from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)
    data_nascimento = models.CharField(max_length=15)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=15)
    bairro = models.CharField(max_length=50)
    rua = models.CharField(max_length=50)
    numero = models.IntegerField()
    cep = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    STATUS =[
        ('DISPONIVEL','DISPONIVEL'),
        ('INDISPONIVEL','INDISPONIVEL'),
    ]
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE)
    placa = models.CharField(max_length=10)
    chassi = models.CharField(max_length=20)
    cor = models.CharField(max_length=15)
    ano = models.IntegerField()
    status = models.CharField(max_length=14, choices=STATUS)


    def __str__(self):
        return self.modelo.nome




class Marcas(models.Model):
    nome = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

class Modelo(models.Model):
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    nome = models.CharField(max_length=10)

    def __str__(self):
        return self.nome


class Alguel(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, null=True, blank=True)
    data_locacao = models.DateField(auto_now=True, null=True, blank=True)
    data_retorno = models.CharField(max_length=15, null=True, blank=True)
    data_recebimento = models.CharField(max_length=25, null=True, blank=True)
    valor = models.CharField(max_length=9, null=True, blank=True)
    observacao = models.TextField(max_length=255, null=True, blank=True)







