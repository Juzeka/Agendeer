from rest_framework.views import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from ..serializers import (
    FuncionarioSerializerAll,
    FuncionarioCreateSerializerAll
)
from ..models import Funcionario
from agendamentos.models import Agendamento
from datetime import date
from ..services import FuncionarioService
from agendamentos.serializers import AgendamentoSerializerAll
from utils.choices import ATIVO
from authentication.services import UserService


class FuncionarioViewSet(ModelViewSet):
    service_class = FuncionarioService
    serializer_class = FuncionarioSerializerAll
    queryset = Funcionario.objects.all()

    def get_funcionario(self, request):
        return Funcionario.objects.filter(user=request.user).first()

    def create(self, request, *args, **kwargs):
        user = UserService(data=request.data).create_user()
        data = dict({**request.data, 'user': user.instance.pk})

        serializer = FuncionarioCreateSerializerAll(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)

        return Response(
            data=serializer.data,
            status=HTTP_201_CREATED,
            headers=headers
        )

    def get_schedulings_today(self, request, *args, **kwargs):
        funcionario = self.get_funcionario(request)
        queryset = Agendamento.objects.filter(
            funcionario=funcionario,
            data=date.today(),
            status=ATIVO
        )
        serializer = AgendamentoSerializerAll(queryset, many=True)

        return Response(serializer.data)

    def get_schedulings_all(self, request, *args, **kwargs):
        funcionario = self.get_funcionario(request)
        queryset = Agendamento.objects.filter(
            funcionario=funcionario,
            status=ATIVO
        )

        serializer = AgendamentoSerializerAll(queryset, many=True)

        return Response(serializer.data)

    def get_schedules_available_date(self, request, *args, **kwargs):
        response = self.service_class(
            pk=request.GET.get('pk'),
            data=request.GET.get('data')
        ).get_horarios_disponiveis_data()

        return Response(data=response, status=HTTP_200_OK)
