from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import permission_required


# Create your views here.

def index(request):
    context = {}
    return render(request, 'app/index.html')

def login(request):
    return render(request, 'app/login.html')

def registro(request):
    return render(request, 'registration/registro.html')

def homeAdmin(request):
    return render(request, 'app/homeadmin.html')

def registro_cliente(request):
    return render(request, 'app/registro-cliente.html')
    
def registro_proveedor(request):
    return render(request, 'app/proveedor/registro-proveedor.html')

def registro_empleado(request):
    return render(request, 'app/empleado/registro-empleado.html')

def recepcion_producto(request):
    return render(request, 'app/recepcion-producto.html')

def boleta_factura(request):
    return render(request, 'app/boleta-factura.html')


# crud servicios
# listar
def servicios(request):
    servicios = Servicio.objects.all()

    data = {
        'servicios': servicios
    }
    return render(request, 'app/servicios/servicios.html', data)

# agregar
def agregar_servicio(request):

    if request.method == 'POST':
        nombre_servicio = request.POST["nombre_servicio"]
        precio_servicio = request.POST["precio_servicio"]
        descripcion = request.POST["descripcion"]

        servicio = Servicio.objects.create(
            nombre_servicio = nombre_servicio,
            precio_servicio = precio_servicio,
            descripcion = descripcion
        )

        servicio.save()
        messages.success(request, 'Servicio registrado correctamente')
        return redirect(to='servicios')

    return render(request, 'app/servicios/agregar-servicio.html')

# eliminar
def eliminar_servicio(request, id):
    try:
        servicio = get_object_or_404(Servicio, id=id)
        servicio.delete()
        messages.success(request, "Eliminado Correctamente")
        return redirect(to='servicios')
    except:
        messages.warning(request, "Error al eliminar")
        servicio = Servicio.objects.all()

        data = {
            'servicio': servicio,
        }

        return render(request, 'app/servicios/servicios.html', data)
    
# editar
def editar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    if request.method == 'POST':
        nombre_servicio = request.POST["nombre_servicio"]
        precio_servicio = request.POST["precio_servicio"]
        descripcion = request.POST["descripcion"]

        servicio.nombre_servicio = nombre_servicio
        servicio.precio_servicio = precio_servicio
        servicio.descripcion = descripcion

        servicio.save()
        return redirect('servicios')
    data = {
        'servicio': servicio
    }
    return  render(request, 'app/servicios/editar-servicio.html', data)
    
# crud reserva de hora
# listar
def reserva_hora(request):
    servicios = Servicio.objects.all()
    facturacion = Facturacion.objects.all()

    data = {
        'servicios': servicios,
        'facturacion': facturacion,
    }
    return render(request, 'app/reserva-hora/reservar-hora.html', data) 