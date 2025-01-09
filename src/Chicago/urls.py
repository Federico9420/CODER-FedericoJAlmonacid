from django.urls import path

from .views import (index, about, Clientes_list, Productos_list, Ventas_list, Producto_create, Ventas_create, Clientes_create,)

app_name = 'Chicago'

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("Clientes/list", Clientes_list, name = "Clientes_list" ),
    path("Clientes/create/", Clientes_create, name = "Clientes_create"),
    path("Producto/list", Productos_list, name ="Productos_list" ),
    path("Producto/create/", Producto_create, name = "Producto_create"),
    path("Ventas/list", Ventas_list, name = "Ventas_list"),
     path("Ventas/create/", Ventas_create, name = "Ventas_Create"),
]
