from django.conf.urls import url
from recetas import views

urlpatterns = [
   url(r'^$', views.indice, name='indice'),
	url(r'^(?P<receta_id>\d+)/$',views.detalle_receta, name='detalle_receta'),
	 url(r'^registro$', views.registro, name='registro'),
    url(r'^login$', views.loginpage, name='login'),
    url(r'^logout$', views.logoutpage, name='logout'),
	 url(r'^addreceta$', views.addreceta, name='addreceta'),	
]
