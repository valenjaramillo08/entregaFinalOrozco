from django.db import models
from datetime import datetime
from writers.models import Writer

# Create your models here.
class Blog(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=254)
    texto = models.CharField(max_length=254)
    categoria = models.CharField(max_length=254)
    extra = models.CharField(blank=True)
    fecha = models.DateTimeField(default=datetime.now(), blank=True)
    url = models.CharField(max_length=254)
    is_publish = models.BooleanField(default=True)
    imagen_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    imagen_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    imagen_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    imagen_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    def __str__(self):
        return self.title