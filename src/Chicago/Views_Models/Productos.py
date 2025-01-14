from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from ..forms import ProductoForm
from ..models import Producto
from django.urls import reverse_lazy    

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    success_url= reverse_lazy('Chicago:Productos_list')

class ProductoDeleteView(DeleteView):
    model= Producto
    form_class = ProductoForm
    success_url= reverse_lazy('Chicago:Productos_list')

class ProductoDetailView(DetailView):
    model= Producto

class ProductoListView(ListView):
    model= Producto

class ProductoUpdateView(UpdateView):
    model= Producto
    form_class = ProductoForm
    success_url= reverse_lazy('Chicago:Productos_list')    