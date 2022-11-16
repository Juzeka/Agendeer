from rest_framework import serializers
from ..models import Agendamento


class AgendamentoSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'
        depth = 2
