#from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('Pagina ', request)

def sobre(request):
    return HttpResponse('Sobre', request)

def contato(request):
    return HttpResponse('Contato', request)