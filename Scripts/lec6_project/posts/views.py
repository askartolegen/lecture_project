from django.shortcuts import render
from .models import *
menu = {'О сайте', "Добавить Статью", "Обратная связь", "Войти"}
# Create your views here.
def home(request):
    posts = Posts.objects.all()
    return render(request, 'home.html', {"title":"Home Page", 'menu':menu, 'posts':posts})
def about(request):
    posts = Posts.objects.all()
    return render(request, 'about.html', {"title":"About Page", 'menu':menu, 'posts':posts})
