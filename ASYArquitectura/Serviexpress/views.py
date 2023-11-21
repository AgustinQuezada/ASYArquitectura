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
# agregar
def reserva_hora(request):
    servicios = Servicio.objects.all()
    facturacion = Facturacion.objects.all()

    data = {
        'servicios': servicios,
        'facturacion': facturacion,
    }

    if request.method == 'POST':
        nombre_cliente = request.POST["nombre_cliente"]
        apellido_cliente = request.POST["apellido_cliente"]
        fecha = request.POST["fecha"]
        servicio = request.POST["servicio"]
        facturacion_cli = request.POST["facturacion"]

        objServicio = Servicio.objects.get(id = servicio)
        objFacturacion = Facturacion.objects.get(id = facturacion_cli)


        reserva_hora = Reserva_hora.objects.create(
            nombre_cliente = nombre_cliente,
            apellido_cliente = apellido_cliente,
            fecha = fecha,
            servicio = objServicio,
            Facturacion = objFacturacion
        )

        reserva_hora.save()
        messages.success(request, 'Reserva exitosa')
        return redirect(to='index')
    
    return render(request, 'app/reserva-hora/reservar-hora.html', data) 

# listar 
def reservas(request):
    reservas = Reserva_hora.objects.all()
    data = {
        'reservas': reservas
    }
    return render(request, 'app/reserva-hora/reservas.html', data)

# editar
def editar_reserva(request, id):
    reserva = get_object_or_404(Reserva_hora, id=id)
    servicios = Servicio.objects.all()
    facturacion = Facturacion.objects.all()

    if request.method == 'POST':
        nombre_cliente = request.POST["nombre_cliente"]
        apellido_cliente = request.POST["apellido_cliente"]
        fecha = request.POST["fecha"]
        servicio = request.POST["servicio"]
        facturacion_cli = request.POST["facturacion"]

        objServicio = Servicio.objects.get(id = servicio)
        objFacturacion = Facturacion.objects.get(id = facturacion_cli)

        reserva.nombre_cliente = nombre_cliente
        reserva.apellido_cliente = apellido_cliente
        reserva.fecha = fecha
        reserva.servicio = objServicio
        reserva.Facturacion = objFacturacion

        reserva.save()
        return redirect('reservas')
    
    data = {
        'reserva': reserva,
        'servicios': servicios,
        'facturacion': facturacion,
    }

    return render(request, 'app/reserva-hora/editar-reserva.html', data)

# eliminar
def eliminar_reserva(request, id):
    try:
        reserva = get_object_or_404(Reserva_hora, id=id)
        reserva.delete()
        messages.success(request, "Eliminado Correctamente")
        return redirect(to='reservas')
    except:
        messages.warning(request, "Error al eliminar")
        reservas = Reserva_hora.objects.all()

        data = {
            'reservas': reservas,
        }

        return render(request, 'app/servicios/servicios.html', data)