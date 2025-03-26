from django.urls import path
from django.views import contato, home, sobre


# Register your models here.

urlpatterns = [
    
    path('', home ),
    path('sobre/', sobre),
    path('contato/', contato),
]