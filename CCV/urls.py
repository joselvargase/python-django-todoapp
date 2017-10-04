from django.conf.urls import url, include

urlpatterns = [
    url(r'^Experimento_1/', include('Experimento_1.urls', namespace='Experimento_1')),
]
