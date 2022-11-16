from django.http import JsonResponse
from rest_framework.views import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_200_OK
from ..serializers import FuncionarioSerializerAll
from ..models import Funcionario
from agendamentos.models import Agendamento
from datetime import date
from ..services import FuncionarioService


class FuncionarioViewSet(ModelViewSet):
    service_class = FuncionarioService
    serializer_class = FuncionarioSerializerAll
    queryset = Funcionario.objects.all()

    def get_funcionario(self, request):
        return Funcionario.objects.filter(user=request.user).first()

    @action(methods=['get'], detail=False)
    def get_schedulings_today(self, request):
        funcionario = self.get_funcionario(request)
        data = Agendamento.objects.filter(
            funcionario=funcionario,
            data=date.today(),
            concluido=False,
            cancelado=False,
            ativo=True
        ).values()

        return JsonResponse(list(data), safe=False)

    @action(methods=['get'], detail=False)
    def get_schedulings_all(self, request):
        funcionario = self.get_funcionario(request)
        data = Agendamento.objects.filter(
            funcionario=funcionario,
            concluido=False,
            cancelado=False,
            ativo=True
        ).values()

        return JsonResponse(list(data), safe=False)

    @action(methods=['get'], detail=False)
    def get_schedules_available_date(self, request):
        response = self.service_class(
            pk=request.GET.get('pk'),
            data=request.GET.get('data')
        ).get_horarios_disponiveis_data()

        return Response(data=response, status=HTTP_200_OK)
