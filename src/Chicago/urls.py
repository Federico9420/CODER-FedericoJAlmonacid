from django.urls import path
from . import views
from Chicago.Views_Models import Ventas, Clientes, Productos
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Chicago'

urlpatterns = [
    # Página principal
    path("", views.index, name="index"),
    # About us
    path("about/", views.about, name="about"),
    # Autenticación
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name="Chicago/logout.html"), name="logout"),
    path('register/', views.CustomRegisterView.as_view(), name='register'),
    path('profile/', views.UpdateProfileView.as_view(), name='profile'),
]

# Clientes
urlpatterns += [
    path("Clientes/list", Clientes.Clientes_list, name="Clientes_list"),
    path("Clientes/create/", Clientes.Clientes_create, name="Clientes_create"),
    path("Clientes/update/<int:pk>", Clientes.Clientes_update, name="Clientes_update"),
    path("Clientes/detail/<int:pk>", Clientes.Clientes_detail, name="Clientes_detail"),
    path("Clientes/confirm/delete/<int:pk>", Clientes.Clientes_delete, name="Clientes_delete"),
]

# Productos
urlpatterns += [
    path("Productos/list", Productos.ProductoListView.as_view(), name="Productos_list"),
    path("Productos/create/", Productos.ProductoCreateView.as_view(), name="Productos_create"),
    path("Productos/update/<int:pk>", Productos.ProductoUpdateView.as_view(), name="Productos_update"),
    path("Productos/detail/<int:pk>", Productos.ProductoDetailView.as_view(), name="Productos_detail"),
    path("Productos/confirm/delete/<int:pk>", Productos.ProductoDeleteView.as_view(), name="Productos_delete"),
]

# Ventas
urlpatterns += [
    path("Ventas/list", Ventas.Ventas_list, name="Ventas_list"),
    path("Ventas/create/", Ventas.Ventas_create, name="Ventas_create"), 
    path("Ventas/update/<int:pk>", Ventas.Ventas_update, name="Ventas_update"),
    path("Ventas/detail/<int:pk>", Ventas.Ventas_detail, name="Ventas_detail"),
    path("Ventas/confirm/delete/<int:pk>", Ventas.Ventas_delete, name="Ventas_delete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)