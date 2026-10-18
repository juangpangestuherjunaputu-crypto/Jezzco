from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    GOAL_CHOICES = [
        ("collaboration", "Mencari partner kolaborasi"),
        ("develop_project", "Mengembangkan proyek"),
        ("find_opportunity", "Mencari peluang"),
        ("share_knowledge", "Berbagi pengetahuan"),
        ("build_business", "Membangun bisnis"),
        ("explore", "Menjelajahi Jezzco"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    full_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Nama lengkap",
    )

    headline = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Headline",
    )

    about = models.TextField(
        blank=True,
        verbose_name="Tentang saya",
    )

    interests = models.TextField(
        blank=True,
        verbose_name="Minat",
        help_text="Contoh: teknologi, bisnis, desain, robotika",
    )

    skills = models.TextField(
        blank=True,
        verbose_name="Keahlian",
        help_text="Contoh: Python, elektronika, desain grafis",
    )

    education = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Pendidikan",
    )

    goal = models.CharField(
        max_length=30,
        choices=GOAL_CHOICES,
        blank=True,
        verbose_name="Tujuan bergabung",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"Profil {self.user.username}"