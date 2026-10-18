from django.contrib import admin
from django.urls import include, path

from core.views import home


urlpatterns = [
    path("admin/", admin.site.urls),
    path("pesan/", include("messaging.urls")),

    path(
        "akun/",
        include("accounts.urls"),
    ),

    path(
        "",
        include("core.urls"),
    ),
]
