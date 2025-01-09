from django.shortcuts import render,redirect

from .models import Producto, Cliente, Venta

from .forms import VentasForm, ProductoForm, ClientesForm

def index(request):
    return render(request, "Chicago/index.html")

def about(request):
    return render(request, "Chicago/about.html")

def Clientes_list(request):
    query = Cliente.objects.all()
    context = {"objects_list": query}
    return render(request, "Chicago/Clientes_list.html", context)

def Clientes_create(request):
    if request.method == "GET":
        form = ClientesForm()
    if request.method == "POST":
        form = ClientesForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect("Chicago:Clientes_list")
        return render(request, "Chicago/Clientes_form.html", {"form": form})

def Productos_list(request):
    query = Producto.objects.all()
    context = {"objects_list": query}
    return render(request, "Chicago/Productos_list.html", context)

def Producto_create(request):
    if request.method == "GET":
        form = ProductoForm()
    if request.method == "POST":
        form = ProductoForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect("Chicago:Productos_list")
        return render(request, "Chicago/Producto_form.html", {"form": form})

def Ventas_list(request):
    query = Venta.objects.all()
    context = {"objects_list": query}
    return render(request, "Chicago/Ventas_list.html", context)

def Ventas_create(request):
    if request.method == "GET":
        form = VentasForm()
    if request.method == "POST":
        form = VentasForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect("Chicago:Ventas_list")
        return render(request, "Chicago/Ventas_form.html", {"form": form})