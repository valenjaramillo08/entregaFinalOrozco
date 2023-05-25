from django.db import models

# Create your models here.
class Writer(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(blank=True)
    email = models.CharField(max_length=254)
    telefono = models.CharField(max_length=254)
    fecha_nacimiento = models.DateField()
    avatar = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre
    