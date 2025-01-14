from django.shortcuts import render,redirect

from ..models import Cliente

from ..forms import ClientesForm

from django.http import HttpResponse, HttpRequest


###


def Clientes_list(request: HttpRequest) -> HttpResponse:
    busqueda = request.GET.get("busqueda")
    if busqueda:
        query = Cliente.objects.filter(nombre__icontains=busqueda)
    else:
         query = Cliente.objects.all()
    return render(request, 'Chicago/Clientes_list.html', {'object_list': query})


###

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


### CLIENTES - UPDATE

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


###  CLIENTES - DETAIL

def Clientes_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Cliente.objects.get(id=pk)
    return render(request, "Chicago/Clientes_detail.html", {"object": query})


### CLIENTES - DELETE

def Clientes_delete (request: HttpRequest, pk: int) -> HttpResponse:
    query = Cliente.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("Chicago:Clientes_list")
    return render(request, 'Chicago/Clientes_confirm_delete.html', {"object": query})