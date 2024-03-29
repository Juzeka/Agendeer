from rest_framework import serializers
from ..models import Funcionario


class FuncionarioSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'
        depth = 2


class FuncionarioCreateSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['user', 'nome_full']
