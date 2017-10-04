from django.conf.urls import url, include

urlpatterns = [
    url(r'^todos4321/', include('todos4321.urls', namespace='todos4321')),
]
