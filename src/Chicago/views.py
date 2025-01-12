from django.shortcuts import render,redirect

from .models import Producto, Cliente, Venta

from .forms import VentasForm, ProductoForm, ClientesForm

from django.http import HttpResponse, HttpRequest

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "Chicago/index.html")

def about(request):
    return render(request, "Chicago/about.html")

# **** CLIENTES

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

def Clientes_update(request: HttpRequest, pk: int) -> HttpResponse:
    query = Cliente.objects.get(id=pk)    
    if request.method == "GET":
        form = ClientesForm(instance=query)
        return render(request, "Chicago/Clientes_form.html", {"form": form})
    if request.method == "POST":
        form = ClientesForm(request.POST, instance=query) 
        if form.is_valid():
            form.save()
            return redirect("Chicago:Clientes_list")
    return render(request, "Chicago/Clientes_form.html", {"form": form})

#**** PRODUCTOS

def Productos_list(request: HttpRequest) -> HttpResponse:
    query = Producto.objects.all()
    context = {"objects_list": query}
    return render(request, "Chicago/Productos_list.html", context)

def Producto_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = ProductoForm()
        return render(request, "Chicago/Producto_form.html", {"form": form})  
    elif request.method == "POST":
        form = ProductoForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect("Chicago:Productos_list")
    return render(request, "Chicago/Producto_form.html", {"form": form})
    
def Producto_update(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        query = Producto.objects.get(id=pk)
    except Producto.DoesNotExist:
        return redirect('Chicago:Productos_list')

    if request.method == "GET":
        form = ProductoForm(instance=query)
        return render(request, "Chicago/Producto_form.html", {"form": form})
    elif request.method == "POST":
        form = ProductoForm(request.POST, instance=query) 
        if form.is_valid():
            form.save()
            return redirect("Chicago:Productos_list")
    return render(request, "Chicago/Producto_form.html", {"form": form})
    
#**** VENTAS

def Ventas_list(request: HttpRequest) -> HttpResponse:
    query = Venta.objects.all()
    context = {"objects_list": query}
    return render(request, "Chicago/Ventas_list.html", context)

def Ventas_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = VentasForm()
        return render(request, "Chicago/Venta_form.html", {"form": form})
    elif request.method == "POST":
        form = VentasForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect("Chicago:Ventas_list")  
        else:
            return render(request, "Chicago/Venta_form.html", {"form": form})
    return render(request, "Chicago/Venta_form.html", {"form": VentasForm()})
    
def Ventas_update(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        query = Venta.objects.get(id=pk)
    except Venta.DoesNotExist:
        return redirect('Chicago:Ventas_list')
    if request.method == "GET":
        form = VentasForm(instance=query) 
        return render(request, "Chicago/Venta_form.html", {"form": form})
    elif request.method == "POST":
        form = VentasForm(request.POST, instance=query) 
        if form.is_valid():
            form.save()
            return redirect("Chicago:Ventas_list") 
        else:
            return render(request, "Chicago/Venta_form.html", {"form": form})
    return render(request, "Chicago/Venta_form.html", {"form": form})

def Ventas_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Venta.objects.get(id=pk)
    return render(request, "Chicago/Ventas_detail.html", {"object": query})

def Ventas_delete (request: HttpRequest, pk: int) -> HttpResponse:
    query = Venta.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("Chicago:Ventas_list")
    return render(request, 'Chicago/Ventas_confirm_delete.html', {"object": query})