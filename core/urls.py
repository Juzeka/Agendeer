from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Documentação",
      default_version='v1',
      description="Descrição<h1>Teste</h1>",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="rafaelgomesalmeida@hotmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('v1/clientes/', include('clientes.urls'), name='clientes'),
    path('v1/funcionarios/', include('funcionarios.urls'), name='funcionarios'),
    path('v1/servicos/', include('servicos.urls'), name='servicos'),
    path('v1/disponibilidades/', include('disponibilidades.urls'), name='disponibilidades'),
    path('v1/agendamentos/', include('agendamentos.urls'), name='agendamentos'),
    path('v1/horarios/', include('horarios.urls'), name='horarios'),
]

urlpatterns += [
    re_path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
