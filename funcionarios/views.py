from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .serializers import FuncionarioSerializerAll
from .models import Funcionario
from agendamentos.models import Agendamento
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication
)
from rest_framework.permissions import IsAuthenticated
from datetime import date


class FuncionarioViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = FuncionarioSerializerAll
    queryset = Funcionario.objects.all()

    @action(methods=['get'], detail=False)
    def agendamentos_today(self, request):
        # import ipdb ; ipdb.set_trace()
        # funcionario = Funcionario.objects.filter(user=request.user).first()
        funcionario = None
        data = Agendamento.objects.filter(
            funcionario=funcionario,
            data=date.today()
        ).values()

        return JsonResponse(list(data), safe=False)

    @action(methods=['get'], detail=False)
    def agendamentos_all(self, request):
        # import ipdb ; ipdb.set_trace()
        # funcionario = Funcionario.objects.filter(user=request.user).first()
        funcionario = None
        data = Agendamento.objects.filter(
            funcionario=funcionario,
        ).values()

        return JsonResponse(list(data), safe=False)