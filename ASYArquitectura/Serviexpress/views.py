from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import permission_required, login_required


# Create your views here.

def index(request):
    context = {}
    return render(request, 'app/index.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='index')
        data['form'] = formulario
    return render(request, 'registration/registro.html', data)

def homeAdmin(request):
    return render(request, 'app/homeadmin.html')

def registro_cliente(request):
    return render(request, 'app/registro-cliente.html')

@permission_required('ServiExpress.view_proveedor')
def proveedores(request):
    proveedores = Proveedor.objects.all()
    data = {
        'proveedores': proveedores
    }
    return render(request, 'app/proveedor/proveedores.html', data)

@permission_required('ServiExpress.add_proveedor')
def registro_proveedor(request):
    rubros = Rubro_proveedor.objects.all()

    data = {
        'rubros': rubros
    }

    if request.method == 'POST':
        nombre_proveedor = request.POST['nombre_proveedor']
        direccion_proveedor = request.POST['direccion_proveedor']
        telefono_proveedor = request.POST['telefono_proveedor']
        correo_proveedor = request.POST['correo_proveedor']
        rubro = request.POST['rubro']

        objRubro = Rubro_proveedor.objects.get(id = rubro)

        proveedor = Proveedor.objects.create(
            nombre_proveedor = nombre_proveedor,
            direccion_proveedor = direccion_proveedor,
            telefono_proveedor = telefono_proveedor,
            correo_proveedor = correo_proveedor,
            rubro = objRubro
        )

        proveedor.save()
        messages.success(request, 'Proveedor registrado correctamente')
        return redirect(to='proveedores')


    return render(request, 'app/proveedor/registro-proveedor.html', data)

@permission_required('ServiExpress.change_proveedor')
def editar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    rubros = Rubro_proveedor.objects.all()
    if request.method == 'POST':
        nombre_proveedor = request.POST['nombre_proveedor']
        direccion_proveedor = request.POST['direccion_proveedor']
        telefono_proveedor = request.POST['telefono_proveedor']
        correo_proveedor = request.POST['correo_proveedor']
        rubro = request.POST['rubro']

        objRubro = Rubro_proveedor.objects.get(id = rubro)

        proveedor.nombre_proveedor = nombre_proveedor
        proveedor.direccion_proveedor = direccion_proveedor
        proveedor.telefono_proveedor = telefono_proveedor
        proveedor.correo_proveedor = correo_proveedor
        proveedor.rubro = objRubro

        proveedor.save()
        return redirect(to='proveedores')
    data = {
        'proveedor': proveedor,
        'rubros': rubros
    }
    return render(request, 'app/proveedor/editar-proveedor.html', data)

@permission_required('ServiExpress.delete_proveedor')
def eliminar_proveedor(request, id):
    try:
        proveedor = get_object_or_404(Proveedor, id=id)
        proveedor.delete()
        messages.success(request, "Eliminado Correctamente")
        return redirect(to='proveedores')
    except:
        messages.warning(request, "Error al eliminar")
        proveedor = Proveedor.objects.all()

        data = {
            'proveedor': proveedor,
        }

        return render(request, 'app/proveedor/proveedores.html', data)

@permission_required('ServiExpress.view_empleado')
def empleados(request):
    empleados = Empleado.objects.all()

    data = {
        'empleados': empleados
    }
    return render(request, 'app/empleado/empleados.html', data)

@permission_required('ServiExpress.add_empleado')
def registro_empleado(request):

    if request.method == 'POST':
        nombre_empleado = request.POST['nombre_empleado']
        apellido_empleado = request.POST['apellido_empleado']
        direccion_empleado = request.POST['direccion_empleado']
        telefono_empleado = request.POST['telefono_empleado']
        correo_empleado = request.POST['correo_empleado']
        fecha_ingreso = request.POST['fecha_ingreso']
        sueldo_base = request.POST['sueldo_base']

        empleado = Empleado.objects.create(
            nombre_empleado = nombre_empleado,
            apellido_empleado = apellido_empleado,
            direccion_empleado = direccion_empleado,
            telefono_empleado = telefono_empleado,
            correo_empleado =  correo_empleado,
            fecha_ingreso = fecha_ingreso,
            sueldo_base = sueldo_base
        )

        empleado.save()
        messages.success(request, 'Empleado registrado correctamente')
        return redirect(to='empleados')
    return render(request, 'app/empleado/registro-empleado.html')

@permission_required('ServiExpress.change_empleado')
def editar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        nombre_empleado = request.POST['nombre_empleado']
        apellido_empleado = request.POST['apellido_empleado']
        direccion_empleado = request.POST['direccion_empleado']
        telefono_empleado = request.POST['telefono_empleado']
        correo_empleado = request.POST['correo_empleado']
        fecha_ingreso = request.POST['fecha_ingreso']
        sueldo_base = request.POST['sueldo_base']

        empleado.nombre_empleado = nombre_empleado
        empleado.apellido_empleado = apellido_empleado
        empleado.direccion_empleado = direccion_empleado
        empleado.telefono_empleado = telefono_empleado
        empleado.correo_empleado = correo_empleado
        empleado.fecha_ingreso = fecha_ingreso
        empleado.sueldo_base = sueldo_base

        empleado.save()
        return redirect(to='empleados')
    data = {
        'empleado': empleado
    }
    return render(request, 'app/empleado/editar-empleado.html', data)

@permission_required('ServiExpress.delete_empleado')
def eliminar_empleado(request, id):
    try:
        empleado = get_object_or_404(Empleado, id=id)
        empleado.delete()
        messages.success(request, "Eliminado Correctamente")
        return redirect(to='empleados')
    except:
        messages.warning(request, "Error al eliminar")
        empleados = Empleado.objects.all()

        data = {
            'empleados': empleados,
        }

        return render(request, 'app/empleado/empleados.html', data)

def recepcion_producto(request):
    return render(request, 'app/recepcion-producto.html')

def boleta_factura(request):
    return render(request, 'app/boleta-factura.html')


# crud servicios
# listar

@permission_required('ServiExpress.view_servicio')
def servicios(request):
    servicios = Servicio.objects.all()

    data = {
        'servicios': servicios
    }
    return render(request, 'app/servicios/servicios.html', data)

# agregar
@permission_required('ServiExpress.add_servicio')
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
@permission_required('ServiExpress.delete_servicio')
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
@permission_required('ServiExpress.change_servicio')
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
@permission_required('ServiExpress.view_reserva_hora')
def reservas(request):
    reservas = Reserva_hora.objects.all()
    data = {
        'reservas': reservas
    }
    return render(request, 'app/reserva-hora/reservas.html', data)

# editar
@permission_required('ServiExpress.change_reserva_hora')
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
@permission_required('ServiExpress.delete_reserva_hora')
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
    
