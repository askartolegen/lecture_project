from django.urls import path
from . import views

urlpatterns = [
    path('addpage/', views.add_page, name='add_page'),
    path('post/<slug:post_slug>', views.show_post, name='post'),
    path('send', views.send_message),
]