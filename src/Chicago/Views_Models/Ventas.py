from django.shortcuts import render,redirect

from ..models import Venta

from ..forms import VentasForm

from django.http import HttpResponse, HttpRequest


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