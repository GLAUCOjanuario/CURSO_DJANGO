from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html', status=200 , context={'name': 'Glauco Januario'}) 

def sobre(request):
    return HttpResponse('Sobre', request)

def contato(request):
    return HttpResponse('Contato', request)

