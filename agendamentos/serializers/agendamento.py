from rest_framework import serializers
from ..models import Agendamento


class AgendamentoSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'


class AgendamentoSerializerResponseCreate(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ['protocolo', 'data', 'horario']
