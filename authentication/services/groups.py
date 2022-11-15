from ..serializers import Group, Permission
from core.permissions import PERMISSIONS_PADRAO


class GroupService:
    def __init__(self) -> None:
        ...

    def criar_grupos_padroes(self):
        for padrao in PERMISSIONS_PADRAO:
            permissions = self.get_permissions_model(
                padrao.get('models_permissions')
            )

            group = Group(**{'name':padrao.get('name')})
            group.save()

            for p in permissions: group.permissions.add(p)

            group.save()

    def get_permissions_model(self, models_permissions):
        permissions = []

        for obj in models_permissions:
            permissions += [
                f'{perm}_{obj.get("model")}'
                for perm in obj.get('permissions')
            ]

        return Permission.objects.filter(codename__in=permissions)
