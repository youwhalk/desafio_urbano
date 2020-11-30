from django.db import models

# Create your models here.

class processo(models.Model):
    pasta = models.CharField(max_length=100)
    comarca = models.CharField(max_length=100)
    uf = models.CharField(max_length=100)

class cadastro_processo(models.Model):
    nome = models.CharField(max_length=200)
    cliente = models.CharField(max_length=200)
    arquivo = models.FileField()
