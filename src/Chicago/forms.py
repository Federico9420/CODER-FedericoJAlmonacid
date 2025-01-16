from django import forms 
from django.contrib.auth.forms import AuthenticationForm
from .models import Cliente, Producto, Venta

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

class VentasForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = "__all__"

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        fields = ["username", "password"]