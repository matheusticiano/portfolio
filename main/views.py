from django.shortcuts import render
from .models import Projeto

def portfolio(request):
    projetos = Projeto.objects.all()
    return render(request, 'main/portfolio.html', {'projetos': projetos})
