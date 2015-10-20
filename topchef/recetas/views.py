from django.shortcuts import get_object_or_404,render
from recetas.models import Receta

# Create your views here.

def indice(request):
   lista_recetas = Receta.objects.all()
   return render(request, 'recetas/index.html', {'lista_recetas': lista_recetas })

def detalle_receta(request,receta_id):
	receta = get_object_or_404(Receta, pk = receta_id)
	return render(request, 'recetas/detalle_receta.html', {'receta': receta })



