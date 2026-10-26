
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import set_language

from .views import (
    home,
    register_view,
    login_view,
    dashboard,
    logout_view,
)

urlpatterns = [
    path("", home, name="home"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("panelim/", dashboard, name="dashboard"),
    path("cikis/", logout_view, name="logout"),
    path("admin/", admin.site.urls),
    path("api/accounts/", include("accounts.urls")),
    path("api/pets/", include("pets.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
]
