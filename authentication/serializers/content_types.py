from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType


class ContentTypeSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'
        depth = 2
