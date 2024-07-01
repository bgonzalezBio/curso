from django.contrib.auth.models import Permission
from rest_framework.serializers import ModelSerializer


class PermissionsSerializer(ModelSerializer):

    class Meta:
        model = Permission
        fields = "__all__"
