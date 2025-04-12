from django import forms
from tiendaApp.models import Producto, Usuario

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'