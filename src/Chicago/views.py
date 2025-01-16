from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpRequest
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.views.generic import CreateView

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "Chicago/index.html")

def about(request):
    return render(request, "Chicago/about.html")

class CustomLoginView(LoginView):
    authentication_form=CustomAuthenticationForm
    template_name= "Chicago/login.html"
    next_page = reverse_lazy("Chicago:index")

class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "Chicago/register.html"
    success_url = reverse_lazy("Chicago:login")
   
    
