from django.urls import path
from .views import * 

urlpatterns = [
	path('', inicio, name ='inicio'),
	path('contacto', contacto, name ='contacto'),
	path('login', login, name ='login'),
	path('agregarproducto', agregarproducto, name ='agregarproducto'),
	path('carrito', carrito, name ='carrito'),
	path('pedidos', pedidos,  name ='pedidos'),
	path('exito', exito,  name ='exito'),
	path('agregarpublicacion', agregarpublicacion,  name ='agregarpublicacion'),
	path('novedades', novedades,  name ='novedades'),
	path('mensajes', mensajes,  name ='mensajes'),
]
