from django.urls import path
from . import views


urlpatterns = [
    path("daftar/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("profil/", views.profile_view, name="profile"),
    path(
        "profil/edit/",
        views.edit_profile_view,
        name="edit_profile",
    ),
    path("logout/", views.logout_view, name="logout"),
]