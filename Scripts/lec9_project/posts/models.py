from django.db import models

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    picture = models.ImageField(default='default value')
    describe = models.TextField(default='DataFlair Django tutorials')

