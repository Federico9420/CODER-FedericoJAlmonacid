from django.shortcuts import render

def index(request):
    return render(request, "Chicago/index.html")

def about(request):
    return render(request, "Chicago/about.html")