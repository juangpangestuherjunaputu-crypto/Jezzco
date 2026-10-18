from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "status",
        "owner",
        "is_published",
        "created_at",
    )

    list_filter = (
        "category",
        "status",
        "is_published",
    )

    search_fields = (
        "title",
        "description",
        "owner__username",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }
