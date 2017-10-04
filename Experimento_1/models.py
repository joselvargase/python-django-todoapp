# coding=utf-8
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

"""
Clase Cliente
"""
class Cliente(models.Model):

    # Fields
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    email = models.EmailField()
    identificacion = models.IntegerField(unique=True, validators=[MinValueValidator(1), MaxValueValidator(2147483647)])
    edad = models.IntegerField(validators=[MinValueValidator(18)])
    ocupacion = models.CharField(max_length=50)
    telefono = models.IntegerField(validators=[MinValueValidator(1111111)])
    sexo = models.CharField(max_length=10)
    direccion = models.CharField(max_length=150)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

"""
Clase Concesionario
"""
class Concesionario(models.Model):
        # Fields
        nombre = models.CharField(max_length=30, validators=[MinLengthValidator(1)], blank=False, unique=True)
        created = models.DateTimeField(auto_now_add=True, editable=False)
        last_updated = models.DateTimeField(auto_now=True, editable=False)
        localizacion = models.CharField(max_length=50)

        class Meta:
            ordering = ('-created',)

        def __unicode__(self):
            return u'%s' % self.pk

        def __str__(self):
            return u'%s' % self.nombre

"""
Clase Vitrina
"""
class Vitrina(models.Model):

    # Fields
    nombre = models.CharField(max_length=30, unique=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    numero_vendedores = models.IntegerField()
    localizacion = models.CharField(max_length=30)

    # Relationship Fields
    concesionario_perteneciente = models.ForeignKey(Concesionario, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return u'%s' % self.nombre

"""
Clase Vehiculo
"""
class Vehiculo(models.Model):

    # Fields
    referencia = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    marca = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    anio_fabricacion = models.PositiveIntegerField()
    tipo_tranmision_choices = (
        ('Manual', 'Manual'),
        ('Automática', 'Automática'))
    tranmision = models.CharField(max_length=30, choices=tipo_tranmision_choices)
    tipo_vehiculo_choices = (
        ('4x4', '4x4'),
        ('4x2', '4x2')
    )
    tipo_vehiculo = models.CharField(max_length=3, choices= tipo_vehiculo_choices)
    pais_ensamblaje_choices = (
        ('Brasil', 'Brasil'),
        ('Argentina', 'Argentina'),
        ('Japón', 'Japón'),
        ('Inglaterra', 'Inglaterra')
    )
    pais_ensamblaje = models.CharField(max_length=11, choices=pais_ensamblaje_choices)
    # Relationship Fields
    vitrina_muestra = models.ForeignKey(Vitrina)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk