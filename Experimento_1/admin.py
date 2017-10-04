from django.contrib import admin

# Register your models here.

from .models import (Cliente, Vehiculo, Concesionario, Vitrina)

admin.site.register(Cliente)
admin.site.register(Vehiculo)
admin.site.register(Concesionario)
admin.site.register(Vitrina)