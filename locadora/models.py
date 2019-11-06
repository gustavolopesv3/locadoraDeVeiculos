from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.IntegerField(max_length=15)
    endereco = models.CharField(max_length=10)