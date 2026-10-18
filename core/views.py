from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProjectForm
from .models import Project


def home(request):
    featured_projects = Project.objects.filter(
        is_published=True
    ).select_related("owner")[:6]

    return render(
        request,
        "core/home.html",
        {
            "featured_projects": featured_projects,
        },
    )


def project_list(request):
    projects = Project.objects.filter(
        is_published=True
    ).select_related("owner")

    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()
    status = request.GET.get("status", "").strip()

    if query:
        projects = projects.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(collaboration_needs__icontains=query)
            | Q(owner__username__icontains=query)
        )

    valid_categories = {
        choice[0] for choice in Project.CATEGORY_CHOICES
    }

    valid_statuses = {
        choice[0] for choice in Project.STATUS_CHOICES
    }

    if category in valid_categories:
        projects = projects.filter(category=category)
    else:
        category = ""

    if status in valid_statuses:
        projects = projects.filter(status=status)
    else:
        status = ""

    context = {
        "projects": projects,
        "query": query,
        "selected_category": category,
        "selected_status": status,
        "categories": Project.CATEGORY_CHOICES,
        "statuses": Project.STATUS_CHOICES,
    }

    return render(
        request,
        "core/project_list.html",
        context,
    )


@login_required
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()

            messages.success(
                request,
                "Proyek kelistrikan berhasil dibuat dan dipublikasikan!",
            )

            return redirect(
                "project_detail",
                slug=project.slug,
            )
    else:
        form = ProjectForm()

    return render(
        request,
        "core/project_form.html",
        {
            "form": form,
            "page_title": "Buat Proyek Electrical Engineering",
            "submit_label": "Publikasikan Proyek",
        },
    )


def project_detail(request, slug):
    project = get_object_or_404(
        Project.objects.select_related("owner"),
        slug=slug,
        is_published=True,
    )

    return render(
        request,
        "core/project_detail.html",
        {"project": project},
    )
