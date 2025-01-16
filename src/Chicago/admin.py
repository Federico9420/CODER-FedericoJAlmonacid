from django.contrib import admin
from .models import Cliente, Producto, Venta, Vendedor

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "stock")

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "telefono")

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ("producto", "vendedor", "cliente", "cantidad", "precio_total", "fecha_venta")
    readonly_fields = ("precio_total", "fecha_venta")

@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ("usuario", "celular")
