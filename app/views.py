from django.shortcuts import render, redirect


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
	return render(request, 'inicio.html')

def contacto(request):
	if request.method == 'POST':
		if request.POST.get('nombre'):
			nombre= request.POST.get('nombre')
			return render(request, 'contacto.html', {'success': 1, 'nombre':nombre})
	

	return render(request, 'contacto.html')

def agregarproducto(request):
	if request.method == 'POST':		
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
		return render(request, 'agregarpublicacion.html', {'success':1})
	return render(request, 'agregarpublicacion.html')	

def novedades(request):
	return render(request, 'novedades.html')	

def mensajes(request):
	return render(request, 'mensajes.html')		