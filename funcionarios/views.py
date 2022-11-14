from django.http import JsonResponse
from rest_framework.views import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_200_OK
from .serializers import FuncionarioSerializerAll
from .models import Funcionario
from agendamentos.models import Agendamento
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication
)
from rest_framework.permissions import IsAuthenticated
from datetime import date
from .services import FuncionarioService


class FuncionarioViewSet(ModelViewSet):
    service_class = FuncionarioService
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = FuncionarioSerializerAll
    queryset = Funcionario.objects.all()

    @action(methods=['get'], detail=False)
    def get_agendamentos_today(self, request):
        # import ipdb ; ipdb.set_trace()
        # funcionario = Funcionario.objects.filter(user=request.user).first()
        funcionario = None
        data = Agendamento.objects.filter(
            funcionario=funcionario,
            data=date.today()
        ).values()

        return JsonResponse(list(data), safe=False)

    @action(methods=['get'], detail=False)
    def get_agendamentos_all(self, request):
        # import ipdb ; ipdb.set_trace()
        # funcionario = Funcionario.objects.filter(user=request.user).first()
        funcionario = None
        data = Agendamento.objects.filter(
            funcionario=funcionario,
        ).values()

        return JsonResponse(list(data), safe=False)

    @action(methods=['get'], detail=False)
    def get_horarios_disponiveis_data(self, request):
        response = self.service_class(
            pk=request.GET.get('pk'),
            data=request.GET.get('data')
        ).get_horarios_disponiveis_data()

        return Response(data=response, status=HTTP_200_OK)