from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpRequest
from .forms import CustomAuthenticationForm

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "Chicago/index.html")

def about(request):
    return render(request, "Chicago/about.html")

class CustomLoginView(LoginView):
    authentication_form=CustomAuthenticationForm
    template_name= "Chicago/login.html"
    next_page = reverse_lazy("Chicago:index")
   
    
