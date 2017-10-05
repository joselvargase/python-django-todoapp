from django import template
from ..models import Cliente, Concesionario, Vehiculo, Vitrina
register = template.Library()

@register.simple_tag
def get_verbose_field_name(instance, field_name):
    """
    Returns verbose_name for a field.
    """
    if instance == 'cliente':
        return Cliente._meta.get_field(field_name).verbose_name.title()
    elif instance == 'concesionario':
        return Concesionario._meta.get_field(field_name).verbose_name.title()
    elif instance == 'vehiculo':
        return Vehiculo._meta.get_field(field_name).verbose_name.title()
    elif instance == 'vitrina':
        return Vitrina._meta.get_field(field_name).verbose_name.title()
    elif instance == 'fk_vitrina':
        return Concesionario.objects.get(id=field_name).nombre
    elif instance == 'fk_vehiculo':
        return Vitrina.objects.get(id=field_name).nombre