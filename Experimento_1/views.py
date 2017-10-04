from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Cliente, Concesionario, Vitrina, Vehiculo
from .forms import ClienteForm, ConcesionarioForm, VitrinaForm, VehiculoForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from django.shortcuts import redirect

def index(request):
    return render(request, 'index.html')

def create_client(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            id = form.cleaned_data['identificacion']
            edad = form.cleaned_data['edad']
            ocupacion = form.cleaned_data['ocupacion']
            telefono = form.cleaned_data['telefono']
            sexo = form.cleaned_data['sexo']
            direccion =  form.cleaned_data['direccion']

            if len(nombre) > 0 and '@' in email and id > 0 and id <= 2147483647 and edad >= 18 \
                    and len(ocupacion) > 0 and 0 < telefono <= 2147483647 and len(sexo) > 0 \
                    and len(direccion) > 0:

                cliente = Cliente(nombre=nombre,
                              email=email,
                              identificacion=id,
                              edad=edad,
                              ocupacion=ocupacion,
                              telefono=telefono,
                              sexo=sexo,
                              direccion=direccion)
                cliente.save()
                messages.success(request,'Se creó exitosamente el cliente')
                return redirect('../listarClientes/')
            else:
                messages.warning(request,'Todos los campos del cliente deben ser debidamente diligenciados')
    else:
        form = ClienteForm()

    return render(request, 'cliente_new_form.html', {'form': form})

def create_concessionaire(request):
    if request.method == 'POST':
        form = ConcesionarioForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            localizacion = form.cleaned_data['localizacion']

            if len(nombre) > 0 and len(localizacion) > 0:

                concesionario = Concesionario(nombre=nombre,
                                          localizacion=localizacion)
                concesionario.save()
                messages.success(request, 'Se creo exitosamente el concesionario')
                return redirect('../listarConcesionarios/')
            else:
                messages.warning(request, 'Todos los campos del concesionario deben ser debidamente diligenciados')
    else:
        form = ConcesionarioForm()
    return render(request, 'concesionario_new_form.html', {'form': form})

@csrf_exempt
def create_vitrina(request):
    if request.method == 'POST':
        form = VitrinaForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            numero_vendedores = form.cleaned_data['numero_vendedores']
            localizacion = form.cleaned_data['localizacion']
            concesionario = Concesionario.objects.get(id=request.POST.get('concesionario_perteneciente', None))
            if len(nombre)>0 and int(numero_vendedores)>0 and len(localizacion)>0 and concesionario is not None:
                vitrina = Vitrina(nombre=nombre,
                                  numero_vendedores=numero_vendedores,
                                  localizacion=localizacion,
                                  concesionario_perteneciente=concesionario)
                vitrina.save()
                messages.success(request, 'Se creo exitosamente la vitrina')
                return redirect('../listarVitrinas/')
            else:
                messages.warning(request, 'Todos los campos de la vitrina deben ser debidamente diligenciados')

    else:
        form = VitrinaForm()
    return render(request, 'vitrina_new_form.html', {'form': form})

def create_vehicle(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            referencia = form.cleaned_data['referencia']
            marca = form.cleaned_data['marca']
            precio = form.cleaned_data['precio']
            anio_fabricacion = form.cleaned_data['anio_fabricacion']
            tranmision = form.cleaned_data['tranmision']
            tipo_vehiculo = form.cleaned_data['tipo_vehiculo']
            pais_ensamblaje = form.cleaned_data['pais_ensamblaje']
            vitrina_muestra = form.cleaned_data['vitrina_muestra']

            if len(referencia)>0 and len(marca)>0 and precio>0.0 and anio_fabricacion>1999 \
                and len(tranmision)>0 and len(tipo_vehiculo)>0 and len(pais_ensamblaje)>0 and vitrina_muestra is not None:

                vehiculo = Vehiculo(referencia=referencia,
                                    marca=marca,
                                    precio=precio,
                                    anio_fabricacion=anio_fabricacion,
                                    tranmision=tranmision,
                                    tipo_vehiculo=tipo_vehiculo,
                                    pais_ensamblaje=pais_ensamblaje,
                                    vitrina_muestra=vitrina_muestra)

                vehiculo.save()
                messages.success(request, 'Se creo exitosamente el vehiculo')
                return redirect('../listarVehiculosTotales/')
            else:
                 messages.warning(request, 'Todos los campos del vehiculo deben ser debidamente diligenciados')
    else:
        form = VehiculoForm()

    return render(request, 'vehiculo_new_form.html', {'form': form})

def cliente_list(request):

    clientes_list = serializers.serialize("python", Cliente.objects.all())
    paginator = Paginator(clientes_list, 2)  # Show 1 clients per page

    page = request.GET.get('page')
    try:
        clientes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        clientes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        clientes = paginator.page(paginator.num_pages)
    return render(request, 'cliente_list.html', {'clientes':clientes})

def go_to_vehiculo_list_template(request):
    vitrinas = Vitrina.objects.all()
    return render(request, 'vehiculo_list.html', {'vitrinas':vitrinas})

def vehiculo_list(request):
    vitrinas = Vitrina.objects.all()
    vehiculos_list = serializers.serialize("python", Vehiculo.objects.all())
    paginator = Paginator(vehiculos_list, 2)  # Show 1 clients per page

    page = request.GET.get('page')
    try:
        vehiculos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        vehiculos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        vehiculos = paginator.page(paginator.num_pages)
    return render(request, 'vehiculo_list.html', {'vehiculos':vehiculos, 'vitrinas':vitrinas, 'title':' - General'})

def vehiculo_list_vitrina_filter(request):
    vitrinas = Vitrina.objects.all()
    if request.method == 'POST':
        id = request.POST['vitrina']
        vitrina_filter = Vitrina.objects.get(id=id)
        vehiculoss_list = Vehiculo.objects.filter(vitrina_muestra=vitrina_filter)
        vehiculos_list = serializers.serialize("python", vehiculoss_list)
        paginator = Paginator(vehiculos_list, 2)  # Show 1 clients per page

        page = request.GET.get('page')
        try:
            vehiculos = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            vehiculos = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            vehiculos = paginator.page(paginator.num_pages)
        return render(request, 'vehiculo_list.html', {'vehiculos': vehiculos, 'vitrinas': vitrinas, 'title': ' - '+vitrina_filter.nombre})

def concesionario_list(request):
    concesionarios_list = serializers.serialize("python", Concesionario.objects.all())
    paginator = Paginator(concesionarios_list, 2)  # Show 1 clients per page

    page = request.GET.get('page')
    try:
        concesionarios = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        concesionarios = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        concesionarios = paginator.page(paginator.num_pages)
    return render(request, 'concesionario_list.html', {'concesionarios': concesionarios})

def vitrina_list(request):
    vitrinas_list = serializers.serialize("python", Vitrina.objects.all())
    paginator = Paginator(vitrinas_list, 2)  # Show 1 clients per page

    page = request.GET.get('page')
    try:
        vitrinas = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        vitrinas = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        vitrinas = paginator.page(paginator.num_pages)
    return render(request, 'vitrina_list.html', {'vitrinas': vitrinas})
