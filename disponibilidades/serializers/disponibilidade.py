from rest_framework import serializers
from ..models import Disponibilidade


class DisponibilidadeSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Disponibilidade
        fields = '__all__'
        depth = 2
