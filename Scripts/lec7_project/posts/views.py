from django.shortcuts import render
from .models import *
from .forms import PostCreate
from django.http import HttpResponse
menu = {'О сайте', "Добавить Статью", "Обратная связь", "Войти"}

# Create your views here.
def home(request):
    posts = Posts.objects.all()
    return render(request, 'home.html', {"title":"Home Page", 'menu':menu, 'posts':posts})
def about(request):
    posts = Posts.objects.all()
    return render(request, 'about.html', {"title":"About Page", 'menu':menu, 'posts':posts})
def addpage(request):
    posts = Posts.objects.all()
    return render(request, 'add_page.html', {"title":"Add Information", 'menu':menu, 'posts':posts})
def contact(request):
    posts = Posts.objects.all()
    return render(request, 'contact.html', {"title":"Reverse connect", 'menu':menu, 'posts':posts})
def login(request):
    posts = Posts.objects.all()
    return render(request, 'login.html', {"title":"Sign In", 'menu':menu, 'posts':posts})

def upload(request):
    upload = PostCreate()
    if request.method == 'POST':
        upload = PostCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('home')
        else:
            return HttpResponse("""Error, reload on <a href ="{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'posts/upload_from.html', {'upload_from':upload})

def update_post(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Posts.objects.get(id=post_id)
    except Posts.DoesNotExist:
        return redirect('home')
    post_form = PostCreate(request.POST or None, instance=post_sel)
    if post_form.is_valid():
        post_form.save()
        return redirect('home')
    return render(request, 'posts/upload_form.html', {'upload_form':post_form})

def delete_post(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Posts.objects.get(id=post_id)
    except Posts.DoesNotExist:
        return redirect('home')
    post_sel.delete()
    return redirect('home')



