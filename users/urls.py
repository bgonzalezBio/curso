from django.urls import path

from users.views.permission_views import PermissionViewSet
from users.views.user_views import UsersView

urlpatterns = [
    path('users', UsersView.as_view({'get': 'list', 'post': 'create'})),
    path('users/<str:pk>', UsersView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('permissions', PermissionViewSet.as_view()),
]
