from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),

    path(
        "proyek/",
        views.project_list,
        name="project_list",
    ),

    path(
        "proyek/buat/",
        views.project_create,
        name="project_create",
    ),

    path(
        "proyek/<slug:slug>/",
        views.project_detail,
        name="project_detail",
    ),
]