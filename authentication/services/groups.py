from ..serializers import GroupCreateSerializer, Permission
from core.permissions import PERMISSIONS_PADRAO


class GroupService:
    def __init__(self) -> None:
        ...

    def criar_grupos_padroes(self):
        grupos = list()

        for padrao in PERMISSIONS_PADRAO:
            data = {'name': padrao.get('name'), 'permissions': list()}
            permissions = self.get_permissions_model(
                padrao.get('models_permissions')
            )

            list_permissions_pks = [perm.pk for perm in permissions]
            data.update({'permissions': list_permissions_pks})

            serializer = GroupCreateSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            grupos.append(serializer.instance)

        return grupos

    def get_permissions_model(self, models_permissions):
        permissions = list()

        for obj in models_permissions:
            permissions += [
                f'{perm}_{obj.get("model")}'
                for perm in obj.get('permissions')
            ]

        return Permission.objects.filter(codename__in=permissions)
