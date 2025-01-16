from django.shortcuts import render

from django.http import HttpResponse, HttpRequest

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "Chicago/index.html")

def about(request):
    return render(request, "Chicago/about.html")

