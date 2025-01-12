from django.shortcuts import render,redirect

from .models import Producto, Cliente, Venta

from .forms import VentasForm, ProductoForm, ClientesForm

from django.http import HttpResponse, HttpRequest

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "Chicago/index.html")

def about(request):
    return render(request, "Chicago/about.html")

def Clientes_list(request: HttpRequest) -> HttpResponse:
    query = Cliente.objects.all()
    context = {"objects_list": query}
    return render(request, 'Chicago/Clientes_list.html', context)

def Clientes_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = ClientesForm()
        return render(request, "Chicago/Clientes_form.html", {"form": form})
    elif request.method == "POST":
        form = ClientesForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect("Chicago:Clientes_list")
        return render(request, "Chicago/Clientes_form.html", {"form": form})
    return render(request, "Chicago/Clientes_form.html", {"form": ClientesForm()})

def Productos_list(request: HttpRequest) -> HttpResponse:
    query = Producto.objects.all()
    context = {"objects_list": query}
    return render(request, "Chicago/Productos_list.html", context)

def Producto_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = ProductoForm()
    if request.method == "POST":
        form = ProductoForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect("Chicago:Productos_list")
        return render(request, "Chicago/Producto_form.html", {"form": form})

def Ventas_list(request: HttpRequest) -> HttpResponse:
    query = Venta.objects.all()
    context = {"objects_list": query}
    return render(request, "Chicago/Ventas_list.html", context)

def Ventas_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = VentasForm()
    if request.method == "POST":
        form = VentasForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect("Chicago:Ventas_list")
        return render(request, "Chicago/Ventas_form.html", {"form": form})