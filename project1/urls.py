from django.urls import path, include

urlpatterns = [
    path('api/token/', include("users.token_urls")),
    path('api/', include("users.urls")),
]