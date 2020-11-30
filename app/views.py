from django.shortcuts import render
from django.http import HttpResponse
import csv


def home(request): #tela1
    return render(request, 'tela1.html')

def index(request): #tela2
    cliente = None
    processo = None
    if request.method=='POST':
        cliente = request.POST['cliente']
        processo = request.POST['processo']
    return render(request, 'tela2.html', {'cliente': cliente, 'processo': processo})

def readfile(request): #função de ler arquivo csv
    with open('C:/Users/outsi/Desktop/desafio/app/processos.csv', 'r') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv, delimiter=';')
        conteudo = []
        for linha in leitor:
              conteudo.append(linha)
              
        return render(request, 'tela3.html', {'conteudo': conteudo})

def tela3(request): #tela3
    return render(request, 'tela3.html')


