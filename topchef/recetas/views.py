from django.shortcuts import get_object_or_404,render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from recetas.models import Receta
from recetas.forms import RecetaForm


# Create your views here.

def indice(request):
   lista_recetas = Receta.objects.all()
   return render(request, 'recetas/index.html', {'lista_recetas': lista_recetas })

def detalle_receta(request,receta_id):
	receta = get_object_or_404(Receta, pk = receta_id)
	return render(request, 'recetas/detalle_receta.html', {'receta': receta })

def registro(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/")
	else:
		form = UserCreationForm()
	return render(request, "recetas/registro.html", {
'form': form,})

def loginpage(request):
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return HttpResponseRedirect("/")
	else:
		form = AuthenticationForm()
	return render(request,'recetas/login.html', {'form': form,})  

def logoutpage(request):
	logout(request)
	return HttpResponseRedirect("/")

def addreceta(request):
	if request.method == "POST":
		form = RecetaForm(request.POST)
		if form.is_valid():
			receta = form.save()
			receta.save()
			return HttpResponseRedirect("/")
	else:
		form = RecetaForm()
	return render(request, 'recetas/add_receta.html', {'form': form})
 



