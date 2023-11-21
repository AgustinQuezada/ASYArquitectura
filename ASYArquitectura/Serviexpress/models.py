from django.db import models

# Create your models here.

class Servicio(models.Model):
  nombre_servicio = models.CharField(max_length=50)
  precio_servicio = models.IntegerField()
  descripcion = models.TextField()

  def __str__(self):
    return self.nombre_servicio
  
class Facturacion(models.Model):
  nombre_facturacion = models.CharField(max_length=50)

  def __str__(self):
    return self.nombre_facturacion
  
class Reserva_hora(models.Model):
  nombre_cliente = models.CharField(max_length=50)
  apellido_cliente = models.CharField(max_length=50)
  fecha = models.DateField()
  servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)
  Facturacion = models.ForeignKey(Facturacion, on_delete=models.PROTECT)

  def __str__(self):
    return self.nombre_cliente
  
class Empleado(models.Model):
  nombre_empleado = models.CharField(max_length=50)
  apellido_empleado = models.CharField(max_length=50)
  direccion_empleado = models.CharField(max_length=60)
  telefono_empleado = models.CharField(max_length=12)
  correo_empleado = models.CharField(max_length=70)
  fecha_ingreso = models.DateField()
  sueldo_base = models.IntegerField()

  def __str__(self):
    return self.nombre_empleado
  
class Rubro_proveedor(models.Model):
  nombre_rubro = models.CharField(max_length=50)

  def __str__(self):
    return self.nombre_rubro
  
class Proveedor(models.Model):
  nombre_proveedor = models.CharField(max_length=50)
  direccion_proveedor = models.CharField(max_length=70)
  telefono_proveedor = models.CharField(max_length=12)
  correo_proveedor = models.CharField(max_length=70)
  rubro = models.ForeignKey(Rubro_proveedor, on_delete=models.PROTECT)

  def __str__(self):
    return self.nombre_proveedor