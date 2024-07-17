from django.db import models
from django.contrib.auth.models import User

class Imagen(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes/')
    fecha = models.DateField()
    nombre_conductor = models.CharField(max_length=100)
    numero_guia = models.CharField(max_length=50)
    lugar_carga = models.CharField(max_length=200)
    kilometraje = models.IntegerField()
    total_carga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Imagen {self.id} - {self.nombre_conductor}"

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]