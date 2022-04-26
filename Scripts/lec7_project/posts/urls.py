from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('update/<int:post_id>', views.update_post),
    path('delete/<int:post_id>', views.delete_post)
]