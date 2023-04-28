from rest_framework import serializers
from django.contrib.auth.models import Group


class GroupSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        depth = 2


class GroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
