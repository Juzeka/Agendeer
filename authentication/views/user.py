from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from ..serializers import (
    User, UserSerializerAll,CreateSimpleUserSerializer
)
from django.contrib.auth.hashers import make_password


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializerAll
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @action(
        methods=['post'],
        detail=False,
        serializer_class=CreateSimpleUserSerializer
    )
    def simple_create(self, request, *args, **kwargs):
        has_pass = make_password(request.data.get('password'))
        request.data.update({'password': has_pass})

        return super().create(request, *args, **kwargs)
