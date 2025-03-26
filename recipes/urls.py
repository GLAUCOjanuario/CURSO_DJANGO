from django.urls import path
from recipes.views import home, contato, sobre  # ✅ certo


# Register your models here.

urlpatterns = [
    
    path('', home ),
    path('sobre/', sobre),
    path('contato/', contato),
]