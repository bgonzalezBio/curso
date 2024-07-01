from rest_framework.viewsets import ModelViewSet

from users.models import BaseUser
from users.serializers.user_serializers import UserSerializer


class UsersView(ModelViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = UserSerializer
