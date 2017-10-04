from django import forms
from .models import Cliente, Vehiculo, Concesionario, Vitrina

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'identificacion', 'edad', 'ocupacion', 'telefono', 'sexo', 'direccion']

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['referencia', 'marca', 'precio', 'anio_fabricacion', 'tranmision', 'tipo_vehiculo','pais_ensamblaje', 'vitrina_muestra']


class ConcesionarioForm(forms.ModelForm):
    class Meta:
        model = Concesionario
        fields = ['nombre', 'localizacion']


class VitrinaForm(forms.ModelForm):
    class Meta:
        model = Vitrina
        fields = ['nombre', 'numero_vendedores', 'localizacion','concesionario_perteneciente']

