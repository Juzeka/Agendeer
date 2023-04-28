from django.contrib import admin
from configuracoes.models import Configuracao
from horarios.models import Horario

admin.site.register(Configuracao)
admin.site.register(Horario)
