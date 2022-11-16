from rest_framework.viewsets import ModelViewSet
from rest_framework.views import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from .serializers import AgendamentoSerializerAll
from .models import Agendamento
from .services import AgendamentoService
from clientes.models import Cliente
from clientes.services import ClienteService


class AgendamentoViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = AgendamentoSerializerAll
    model_class = Agendamento

    def get_queryset(self):
        return self.model_class.objects.filter(ativo=True)

    def create(self, request, *args, **kwargs):
        cliente = Cliente.objects.filter(
            pk=request.data.get('cliente')
        ).first()

        if not isinstance(cliente, Cliente):
            data = request.data
            cliente = ClienteService(
                nome_full=data.get('nome_full'),
                whatsapp=data.get('whatsapp')
            ).new_cliente_em_agendamento()

        request.data.update({'cliente': cliente.pk})

        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        super().perform_create(serializer)

        instance = serializer.instance

        AgendamentoService(
            data=instance.data,
            horario=instance.horario,
            funcionario=instance.funcionario.pk
        ).desativar_horario_data_funcionario()

    def set_cancel(self, agendamento):
        agendamento.cancelado = True
        agendamento.ativo = False

        AgendamentoService(
            data=agendamento.data,
            horario=agendamento.horario,
            funcionario=agendamento.funcionario.pk
        ).ativar_horario_data_funcionario()

        agendamento.save()

    @action(methods=['get'], detail=False)
    def cancel_user(self, request):
        try:
            cliente = Cliente.objects.filter(
                whatsapp=request.data.get('whatsapp')
            ).first()
            agendamento = get_object_or_404(
                self.model_class,
                cliente=cliente.pk
            )

            self.set_cancel(agendamento)

            return Response(
                data={
                    'mensage': 'Agendamento cancelado com sucesso!'
                },
                status=HTTP_200_OK
            )
        except ValidationError as e:
            return Response(
                data={
                    'mensage': 'Usúario incorreto ou não existe!'
                },
                status=HTTP_404_NOT_FOUND
            )

    @action(methods=['get'], detail=True)
    def cancel(self, request, pk):
        agendamento = get_object_or_404(self.model_class, pk=pk)

        self.set_cancel(agendamento)

        return Response(
            data={
                'mensage': 'Agendamento cancelado com sucesso!'
            },
            status=HTTP_200_OK
        )

    @action(methods=['get'], detail=True)
    def finish(self, request, pk):
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
