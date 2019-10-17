from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def inicio(request):
	# if this is a POST request we need to process the form data
	if request.method == 'GET':
		if request.GET.get('nombre'):
			nombre= request.GET.get('nombre')
			return render(request, 'inicio.html', {"nombre": nombre})

	if request.method == 'POST':
		if request.POST.get('agregar'):
			return render(request, 'inicio.html', {"producto": 1})
	contexto= {}
	contexto['productos']= Productos.objects.all()		
	return render(request, 'inicio.html', contexto)

def contacto(request):
	if request.method == 'POST':
		if request.POST.get('nombre'):
			nombre = request.POST.get('nombre')
			correo = request.POST.get('correo')
			mensaje = request.POST.get('mensaje')
			foto = request.FILES['foto']
			mensaje= Mensajes(nombre=nombre, correo=correo, mensaje=mensaje, foto=foto )
			mensaje.save()
			return render(request, 'contacto.html', {'success': 1, 'nombre':nombre})
	

	return render(request, 'contacto.html')

def agregarproducto(request):
	if request.method == 'POST':
		nombre = request.POST.get('nombre')
		valor = request.POST.get('valor')
		color = request.POST.get('color')
		tipo = request.POST.get('tipo')
		stock = request.POST.get('stock')
		foto = request.FILES['foto']
		producto = Productos(nombre=nombre, valor=valor, color=color, tipo=tipo, stock=stock, foto=foto)
		producto.save()
		return render(request, 'agregarproducto.html', {'success':1})
	return render(request, 'agregarproducto.html')	

def login(request):
	if request.method == 'POST':
		nombre= request.POST.get('nombre')
		redir= 'inicio/' + nombre
		return redirect('/?nombre=' + nombre)
	return render(request, 'login.html')

def carrito(request):
	if request.method == 'POST':
		
		return redirect('exito')
	return render(request, 'carrito.html')	

def pedidos(request):
	return render(request, 'pedidos.html')	


def exito(request):
	return render(request, 'exito.html')	

def agregarpublicacion(request):
	if request.method == 'POST':
		titulo = request.POST.get('titulo')
		cuerpo = request.POST.get('cuerpo')		
		novedad = Novedades(titulo=titulo, cuerpo=cuerpo)
		novedad.save()
		return render(request, 'agregarpublicacion.html', {'success':1})
	return render(request, 'agregarpublicacion.html')	

def novedades(request):
	contexto = {}
	contexto['novedades'] = Novedades.objects.all()

	return render(request, 'novedades.html', contexto)	

def mensajes(request):
	contexto= {}
	contexto['mensajes']= Mensajes.objects.all()

	return render(request, 'mensajes.html', contexto)		