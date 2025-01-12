from django.urls import path

from . import views

app_name = 'Chicago'

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("Clientes/list", views.Clientes_list, name = "Clientes_list" ),
    path("Clientes/create/", views.Clientes_create, name = "Clientes_create"),
    path("Clientes/update/<int:pk>", views.Clientes_update, name = "Clientes_update"),
    path("Producto/list", views.Productos_list, name ="Productos_list" ),
    path("Producto/create/", views.Producto_create, name = "Producto_create"),
    path("Producto/update/<int:pk>", views.Producto_update, name = "Producto_update"),
    path("Ventas/list", views.Ventas_list, name = "Ventas_list"),
    path("Ventas/create/", views.Ventas_create, name = "Ventas_Create"),
    path("Ventas/update/<int:pk>", views.Ventas_update, name = "Ventas_update"),
    path("Ventas/detail/<int:pk>", views.Ventas_detail, name = "Ventas_detail"),
    path("Ventas/confirm/delete/<int:pk>", views.Ventas_delete, name = "Ventas_delete"),

]
