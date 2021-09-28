from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    dados = DadosSite.objects.all()
    produtos = Produto.objects.all()
    pessoas = Pessoa.objects.all()

    dicionario = {
        "dados_site": dados,
        "lista_produtos" : produtos,
        "lista_pessoas" : pessoas
    }

    return render(request, "index.html", dicionario)