from django.contrib import admin
from .models import Cliente, Producto, Venta


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "telefono") 

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "stock")

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cliente', 'cantidad', 'total', 'fecha')
    readonly_fields = ('total',)

