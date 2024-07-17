from django import forms
from .models import Imagen

class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ['imagen', 'fecha', 'nombre_conductor', 'numero_guia', 'lugar_carga', 'kilometraje', 'total_carga']