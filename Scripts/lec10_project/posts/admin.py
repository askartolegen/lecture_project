from django.contrib import admin
from .models import *

# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Posts, PostsAdmin)
