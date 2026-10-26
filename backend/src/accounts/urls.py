
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import RegisterView, MeView


app_name = "accounts"

urlpatterns = [
    # Yeni kullanıcı kaydı
    path(
        "register/",
        RegisterView.as_view(),
        name="register",
    ),

    # Kullanıcı girişi ve JWT token alma
    path(
        "login/",
        TokenObtainPairView.as_view(),
        name="login",
    ),

    # Access token yenileme
    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),

    # Giriş yapan kullanıcının profili
    path(
        "me/",
        MeView.as_view(),
        name="me",
    ),
]
