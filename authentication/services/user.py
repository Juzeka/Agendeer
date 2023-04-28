from authentication.serializers import CreateUserSerializer


class UserService:
    def __init__(self, *args, **kwargs):
        self.data = kwargs.get('data')

    def create_user(self):
        data = dict(self.data)
        data.update({'groups': [data.get('groups')]})

        serializer = CreateUserSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return serializer

