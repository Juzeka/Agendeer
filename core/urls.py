from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib import admin


urlpatterns = [
    path('admin', admin.site.urls), #temporario
    path(
        'api/auth/',
        include('authentication.urls'),
        name='auth'
    ),
    path(
        'api/mgt/clients/',
        include('clientes.urls'),
        name='clients'
    ),
    path(
        'api/mgt/schedulings/',
        include('agendamentos.urls'),
        name='schedulings'
    ),
    path(
        'api/mgt/settings/',
        include('configuracoes.urls'),
        name='settings'
    ),
    path(
        'api/mgt/availabilities/',
        include('disponibilidades.urls'),
        name='availabilities'
    ),
    path(
        'api/mgt/officials/',
        include('funcionarios.urls'),
        name='officials'
    ),
    path(
        'api/mgt/schedules/',
        include('horarios.urls'),
        name='schedules'
    ),
    path(
        'api/mgt/services/',
        include('horarios.urls'),
        name='services'
    ),
]

urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'doc/api/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
]
