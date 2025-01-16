from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.forms import BaseModelForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpRequest
from .forms import CustomAuthenticationForm, CustomUserCreationForm, UserProfileForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_not_required #type: ignore
from django.utils.decorators import method_decorator
#@login_required

@login_not_required
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "Chicago/index.html")

@login_not_required
def about(request):
    return render(request, "Chicago/about.html")

class CustomLoginView(LoginView):
    authentication_form=CustomAuthenticationForm
    template_name= "Chicago/login.html"
    next_page = reverse_lazy("Chicago:index")

@method_decorator(login_not_required, name= 'dispatch')
class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "Chicago/register.html"
    success_url = reverse_lazy("Chicago:login")

    def form_valid(self, form:BaseModelForm) -> HttpResponse:
        messages.success(self.request, 'Registo exitoso. Ahora puedes iniciar sesión.')
        return super().form_valid(form)

@login_not_required
class UpdateProfileView (UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "Chicago/profile.html"
    success_url = reverse_lazy('Chicago:index')

    def get_object(self):
        return self.request.user
    
