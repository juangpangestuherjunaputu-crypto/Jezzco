from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Project(models.Model):

    CATEGORY_CHOICES = [
        ("fundamentals", "Electrical Fundamentals"),
        ("electronics", "Electronic Circuits"),
        ("industrial", "Industrial Electrical"),
        ("control", "Control Systems"),
        ("energy", "Power & Energy"),
        ("iot", "Embedded Systems & IoT"),
        ("machines", "Electrical Machines"),
        ("research", "Research & Innovation"),
    ]

    STATUS_CHOICES = [
        ("idea", "Ide Awal"),
        ("development", "Sedang Dikembangkan"),
        ("prototype", "Prototipe"),
        ("launched", "Sudah Diluncurkan"),
    ]

    title = models.CharField(
        max_length=150,
        verbose_name="Judul Proyek",
    )

    slug = models.SlugField(
        max_length=170,
        unique=True,
        blank=True,
    )

    description = models.TextField(
        verbose_name="Deskripsi Proyek",
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default="fundamentals",
        verbose_name="Kategori Kelistrikan",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="idea",
        verbose_name="Tahap Proyek",
    )

    collaboration_needs = models.TextField(
        blank=True,
        verbose_name="Kebutuhan Kolaborasi",
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects",
        verbose_name="Pemilik Proyek",
    )

    is_published = models.BooleanField(
        default=True,
        verbose_name="Dipublikasikan",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Proyek"
        verbose_name_plural = "Proyek"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title) or "proyek"
            candidate = base_slug
            counter = 2

            while Project.objects.filter(slug=candidate).exists():
                candidate = f"{base_slug}-{counter}"
                counter += 1

            self.slug = candidate

        super().save(*args, **kwargs)
