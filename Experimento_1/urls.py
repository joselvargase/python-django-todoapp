from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^crearCliente/$', views.create_client, name='crearCliente'),
    url(r'^crearConcesionario/$', views.create_concessionaire, name='crearConcesionario'),
    url(r'^crearVitrina/$', views.create_vitrina, name='crearVitrina'),
    url(r'^crearVehiculo/$', views.create_vehicle, name='crearVehiculo'),
    url(r'^listarClientes/$', views.cliente_list, name='listarClientes'),
    url(r'^listarVehiculos/$', views.go_to_vehiculo_list_template, name='listarVehiculos'),
    url(r'^listarVehiculosTotales/$', views.vehiculo_list, name='listarVehiculosTotales'),
    url(r'^listarVehiculosPorVitrina/$', views.vehiculo_list_vitrina_filter, name='listarVehiculosPorVitrina'),
    url(r'^listarConcesionarios/$', views.concesionario_list, name='listarConcesionarios'),
    url(r'^listarVitrinas/$', views.vitrina_list, name='listarVitrinas')
]
