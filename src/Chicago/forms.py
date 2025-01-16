from django import forms 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
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

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        help_texts = {'username': ''}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        