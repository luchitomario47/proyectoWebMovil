from django.shortcuts import render

from productos.models import Producto

def mostarIndex(request):
    return render(request, 'index.html')

def mostarListado(request):
    productos = Producto.objects.all().values()
    datos = {'productos' : productos}
    return render(request, 'listado.html', datos)

def mostarActualizar(request, id):
    try:
        producto = Producto.objects.get(id=id)
        datos = {'producto': producto}
        return render(request, 'form_actualizar.html', datos)
    except:
        productos = Producto.objects.all().values()
        datos = {
            'productos': productos,
            'r2': 'El ID ('+str(id)+') no existe'
        }
        return render(request, 'listado.html', datos)

def mostarResgistrar(request):
    return render(request, 'form_registrar.html')

def insertarProducto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        detalle = request.POST['detalle']
        producto = Producto(nombre = nombre, precio = precio, detalle = detalle)
        producto.save()
        datos = { 'r' : 'Registro realizado correctamente'}
        return render(request, 'form_registrar.html', datos)
    else:
        datos = { 'r2' : 'No se puede procesar la solicitud'}
        return render(request, 'form_registrar.html', datos)

def actualizarProducto(request, id):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        detalle = request.POST['detalle']
        
        producto = Producto.objects.get(id=id)
        producto.nombre = nombre
        producto.precio = precio
        producto.detalle = detalle
        producto.save()
        
        productos = Producto.objects.all().values()
        datos = {
            'productos': productos,
            'r': 'Datos modificados correctamente'
        }
        return render(request, 'listado.html', datos)
    else:
        datos = {'r2': 'No se puede procesar la solicitud'}
        return render(request, 'form_registrar.html', datos)

def eliminarProducto(request, id):
    try:
        producto = Producto.objects.get(id = id)
        producto.delete()
        productos = Producto.objects.all().values()
        datos = {
            'productos': productos,
            'r' : 'Registro eliminado correctamente'
        }
        return render(request, 'listado.html', datos)
    except:
        productos = Producto.objects.all().values()
        datos = {
            'productos': productos,
            'r2' : 'El ID ('+str(id)+' no existe. Imposible eliminar)'
        }
        return render(request, 'listado.html', datos)
    
def mantencion(request):
    return render(request, 'mantencion.html')