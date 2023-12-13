from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('homeAdmin/', views.homeAdmin, name='homeAdmin'),
    path('registro-cliente/', views.registro_cliente, name='registro-cliente'),
    path('proveedores/', views.proveedores, name='proveedores'),
    path('registro-proveedor/', views.registro_proveedor, name='registro-proveedor'),
    path('editar-proveedor/<int:id>/', views.editar_proveedor, name='editar-proveedor'),
    path('eliminar-proveedor/<int:id>/', views.eliminar_proveedor, name='eliminar-proveedor'),
    path('empleados/', views.empleados, name='empleados'),
    path('registro-empleado/', views.registro_empleado, name='registro-empleado'),
    path('editar-empleado/<int:id>/', views.editar_empleado, name='editar-empleado'),
    path('eliminar-empleado/<int:id>/', views.eliminar_empleado, name='eliminar-empleado'),
    path('recepcion-producto/', views.recepcion_producto, name='recepcion-producto'),
    path('boleta-factura/', views.boleta_factura, name='boleta-factura'),
    path('servicios/', views.servicios, name='servicios'),
    path('agregar-servicio/', views.agregar_servicio, name='agregar-servicio'),
    path('eliminar-servicio/<int:id>/', views.eliminar_servicio, name='eliminar-servicio'),
    path('editar-servicio/<int:id>/', views.editar_servicio, name='editar-servicio'),
    path('reservas/', views.reservas, name='reservas'),
    path('reserva-hora/', views.reserva_hora, name='reserva-hora'),
    path('editar-reserva/<int:id>/', views.editar_reserva, name='editar-reserva'),
    path('eliminar-reserva/<int:id>/', views.eliminar_reserva, name='eliminar-reserva'),
]