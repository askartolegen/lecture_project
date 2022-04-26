from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import AddPostForm
from django.core.mail import send_mail
# Create your views here.
def show_post(request, post_slug):
    post = get_object_or_404(Posts, slug=post_slug)
    context = {'post': post}
    return render(request, 'posts/post.html', context=context)

def send_message(request):
    send_mail('Web Programming: Back End', 'My content',
              "askartolegen13@gmail.com",
              ["askartolegen13@gmail.com", "180103143@stu.sdu.edu.kz"],
              fail_silently=False, html_message="<b>Bold text</b><i> Italic text</i>")
    return render(request, 'posts/successfull.html')

def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('add_page')
            except:
                form.add_error(None, "Error while add posts")
    else:
        form = AddPostForm()

    return render(request, 'posts/addpage.html', {'title': 'Add Posts', 'form': form})
