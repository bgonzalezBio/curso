from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        return 9 in request.user.user_permissions.all().values_list('id', flat=True)
