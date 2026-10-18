from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

from .models import UserProfile
from .forms import UserProfileForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            # Memastikan profil tersedia untuk akun baru.
            UserProfile.objects.get_or_create(user=user)

            login(request, user)

            messages.success(
                request,
                "Selamat datang di Jezzco! Lengkapi profilmu."
            )

            return redirect("edit_profile")

    else:
        form = UserCreationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form},
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(
                request,
                "Kamu berhasil masuk ke Jezzco!"
            )

            return redirect("profile")

    else:
        form = AuthenticationForm(request)

    return render(
        request,
        "accounts/login.html",
        {"form": form},
    )


@login_required
def profile_view(request):
    profile, _ = UserProfile.objects.get_or_create(
        user=request.user
    )

    return render(
        request,
        "accounts/profile.html",
        {"profile": profile},
    )


@login_required
def edit_profile_view(request):
    profile, _ = UserProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        form = UserProfileForm(
            request.POST,
            instance=profile,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Profil Jezzco berhasil diperbarui!"
            )

            return redirect("profile")

    else:
        form = UserProfileForm(instance=profile)

    return render(
        request,
        "accounts/edit_profile.html",
        {"form": form},
    )


@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)

        messages.success(
            request,
            "Kamu berhasil keluar dari Jezzco."
        )

        return redirect("home")

    return redirect("profile")