from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "home.html", {"name":"Madina", "age":20})

def about(request):
    return render(request, "about.html")