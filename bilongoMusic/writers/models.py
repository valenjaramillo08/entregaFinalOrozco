from django.db import models

# Create your models here.
class Writer(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion_general = models.CharField(blank=True)
    descripcion = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    telefono = models.CharField(max_length=254)
    fecha_nacimiento = models.DateField()
    titulo = models.CharField(max_length=254,default='no_data')
    avatar = models.ImageField(upload_to='photos/%Y/%m/%d/')
    def __str__(self):
        return self.nombre
    