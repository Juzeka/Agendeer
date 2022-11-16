from django.urls import path, include
from rest_framework.routers import SimpleRouter
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from authentication.views import (
    ContentTypeViewSet,
    GroupViewSet,
    PermissionViewSet,
    UserViewSet
)
from agendamentos.views import AgendamentoViewSet
from clientes.views import ClienteViewSet
from configuracoes.views import ConfiguracaoViewSet
from disponibilidades.views import DisponibilidadeViewSet
from funcionarios.views import FuncionarioViewSet
from horarios.views import HorarioViewSet
from servicos.views import ServicoViewSet


routers = SimpleRouter()

routers.register(r'auth/users', UserViewSet, basename='users')
routers.register(r'auth/permissions', PermissionViewSet, basename='permissions')
routers.register(r'auth/groups', GroupViewSet, basename='groups')
routers.register(r'auth/apps', ContentTypeViewSet, basename='apps')
routers.register(r'schedulings', AgendamentoViewSet, basename='agendamentos')
routers.register(r'mgt/clients', ClienteViewSet, basename='clientes')
routers.register(r'mgt/settings', ConfiguracaoViewSet, basename='configuracoes')
routers.register(r'mgt/availabilities', DisponibilidadeViewSet, basename='disponibilidades')
routers.register(r'mgt/officials', FuncionarioViewSet, basename='funcionarios')
routers.register(r'mgt/schedules', HorarioViewSet, basename='horarios')
routers.register(r'mgt/services', ServicoViewSet, basename='servicos')


from django.contrib import admin

urlpatterns = [
    path('admin', admin.site.urls), #temporario
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(routers.urls), name='api'),
]

urlpatterns += [
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
