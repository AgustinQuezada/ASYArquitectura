from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reserva-hora/', views.reserva_hora, name='reserva-hora'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('homeAdmin/', views.homeAdmin, name='homeAdmin'),
    path('registro-cliente/', views.registro_cliente, name='registro-cliente'),
    path('registro-proveedor/', views.registro_proveedor, name='registro-proveedor'),
    path('registro-empleado/', views.registro_empleado, name='registro-empleado'),
    path('recepcion-producto/', views.recepcion_producto, name='recepcion-producto'),
    path('boleta-factura/', views.boleta_factura, name='boleta-factura'),
    path('servicios/', views.servicios, name='servicios'),
    path('agregar-servicio/', views.agregar_servicio, name='agregar-servicio'),
    path('eliminar-servicio/<int:id>/', views.eliminar_servicio, name='eliminar-servicio'),
]