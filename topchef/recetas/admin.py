from django.contrib import admin
from recetas.models import Receta
from recetas.models import Ingrediente

# Register your models here.

admin.site.register(Receta)
admin.site.register(Ingrediente)
