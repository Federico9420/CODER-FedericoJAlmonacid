from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

class Vendedor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendedor')
    celular = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="Imagenes_Perfil", blank=True, null=True)

    def __str__(self):
        return self.usuario.username

class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    fecha_venta = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ("-fecha_venta",)

    def clean(self):
        if self.cantidad > self.producto.stock:
            raise ValidationError("La cantidad vendida no puede ser superior al stock.")

    def save(self, *args, **kwargs):
        self.precio_total = self.producto.precio * self.cantidad
        self.producto.stock -= self.cantidad
        self.producto.save()
        super().save(*args, **kwargs)
