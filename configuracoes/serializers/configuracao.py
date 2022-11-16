from rest_framework import serializers
from ..models import Configuracao


class ConfiguracaoSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Configuracao
        fields = '__all__'
        depth = 2
