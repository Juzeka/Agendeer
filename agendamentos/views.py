from rest_framework.viewsets import ModelViewSet
from rest_framework.views import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .serializers import AgendamentoSerializerAll
from .models import Agendamento
from .services import AgendamentoService


class AgendamentoViewSet(ModelViewSet):
    serializer_class = AgendamentoSerializerAll
    model_class = Agendamento

    def get_queryset(self):
        return self.model_class.objects.filter(ativo=True)

    def perform_create(self, serializer):
        super().perform_create(serializer)

        instance = serializer.instance

        AgendamentoService(
            data=instance.data,
            horario=instance.horario,
            funcionario=instance.funcionario.pk
        ).desativar_horario_data_funcionario()

    @action(methods=['get'], detail=True)
    def cancelar(self, request, pk):
        agendamento = get_object_or_404(self.model_class, pk=pk)

        agendamento.cancelado = True
        agendamento.ativo = False

        AgendamentoService(
            data=agendamento.data,
            horario=agendamento.horario,
            funcionario=agendamento.funcionario.pk
        ).ativar_horario_data_funcionario()

        agendamento.save()

        return Response(
            data={
                'mensage': 'Agendamento cancelado com sucesso!'
            },
            status=HTTP_200_OK
        )

    @action(methods=['get'], detail=True)
    def concluir(self, request, pk):
        agendamento = get_object_or_404(Agendamento, pk=pk)

        agendamento.ativo = False
        agendamento.concluido = True

        agendamento.save()

        return Response(
            data={
                'mensage': 'Agendamento concluido com sucesso!'
            },
            status=HTTP_200_OK
        )