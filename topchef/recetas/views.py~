from django.shortcuts import render
from recetas.models import Receta

# Create your views here.

def indice(request):
   lista_recetas = Receta.objects.all()
   return render(request, 'recetas/index.html', {'lista_recetas': lista_recetas })


