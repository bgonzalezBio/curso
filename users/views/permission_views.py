from django.contrib.auth.models import Permission
from rest_framework.generics import ListAPIView

from project1.permissions import UserPermission
from users.serializers.permission_serializers import PermissionsSerializer


class PermissionViewSet(ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionsSerializer
    # permission_classes = [UserPermission]
