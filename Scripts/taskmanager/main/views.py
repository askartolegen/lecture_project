from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title':'Главная Страница Сайта', 'tasks':tasks})

def about(request):
    return render(request, 'main/about.html',  {'title':'Информация про нас'})

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = "Форма была неверной"

    form = TaskForm()
    context = {
        'title': 'Создать таск',
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
