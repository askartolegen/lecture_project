from django.db import models
from django.urls import reverse
# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    is_published = models.BooleanField(default=True, verbose_name='Qwerty')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def get_number(self):
        return 7

    def get_title(self):
        return self.title
