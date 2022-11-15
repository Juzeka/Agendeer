from rest_framework import serializers
from django.contrib.auth.models import Permission


class PermissionSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
        depth = 2
