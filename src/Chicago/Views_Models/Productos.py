from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from ..forms import ProductoForm
from ..models import Producto
from django.urls import reverse_lazy    

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    success_url= reverse_lazy("Chicago:Productos_list")

class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('Chicago:Productos_list')

class ProductoUpdateView(UpdateView):
    model= Producto
    form_class = ProductoForm
    success_url= reverse_lazy("Chicago:Productos_list")    

class ProductoListView(ListView):
    model= Producto

    def get_queryset(self):

        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            query = Producto.objects.filter(nombre__icontains=busqueda)
        else:
            query = Producto.objects.all()
        return query

class ProductoDetailView(DetailView):
    model= Producto
    