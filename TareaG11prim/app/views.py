from django.shortcuts import render, redirect
from .models import *
#esto es mientras 
carrito_key=0
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
			if request.FILES:
				foto = request.FILES['foto']
			else:
				foto=None	
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
	contexto= {}
	carro =Carro.objects.filter(pk=carrito_key).first()
	contexto['carro'] = carro
	if carro:
		contexto['productos']= contexto['carro'].productos.all()
		valor= 0
		for p in contexto['productos']:
			valor += p.valor
		contexto['valor']= valor	
	
	if request.method == 'POST':
		nombre = request.POST.get('nombre')
		correo = request.POST.get('correo')
		ciudad = request.POST.get('ciudad')
		contexto['nombre'] = nombre
		contexto['correo'] = correo
		contexto['ciudad'] = ciudad
		pedido= Pedidos(carrito=contexto['carro'], nombre=nombre, correo=correo, ciudad=ciudad, precio=valor)
		pedido.save()
		carro.activo = False

		return render(request, 'exito.html', contexto)
		
	return render(request, 'carrito.html', contexto)	

def pedidos(request):
	contexto= {}
	pedidos = Pedidos.objects.filter(finalizado = False)
	print(pedidos)
	contexto['pedidos'] = pedidos
	return render(request, 'pedidos.html',contexto)	


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

def borrarmensaje(request):	
	if request.method == 'POST':
		mensaje = request.POST.get('mensaje')
		m = Mensajes.objects.filter(pk=mensaje)
		m.delete()
	return redirect('/mensajes')

def borrarencarrito(request):
	if request.method == 'POST':
		producto = request.POST.get('producto')
		carro = request.POST.get('carro')
		#revisar esto
		c = Carro.objects.filter(pk=carro).first()
		p = Productos.objects.filter(pk=producto).first()
		c.productos.remove(p)	
	return redirect('/carrito')

def agregarcarrito(request):
	if request.method == 'POST':
		producto = request.POST.get('producto')
		p= Productos.objects.filter(pk=producto).first()
		c = Carro.objects.filter(pk=carrito_key).first()
		if not c:
			c= Carro(pk=carrito_key)
			c.save()	
		c.productos.add(p)
		c.save()
	return redirect('/')

def finalizarpedido(request):
	if request.method == 'POST':
		pedido = request.POST.get('pedido')
		p = Pedidos.objects.filter(pk=pedido).first()
		p.finalizado = True
		p.save()
	return redirect('/pedidos')



