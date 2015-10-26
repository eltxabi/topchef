from django.conf.urls import url
from recetas import views

urlpatterns = [
   url(r'^$', views.indice, name='indice'),
	url(r'^(?P<receta_id>\d+)/$',views.detalle_receta, name='detalle_receta'),
]
