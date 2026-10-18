from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        fields = [
            "title",
            "description",
            "category",
            "status",
            "collaboration_needs",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "category": "Bidang Electrical Engineering",
            "status": "Tahap Perkembangan",
            "collaboration_needs": "Kebutuhan Kolaborasi",
        }

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Contoh: Sistem Monitoring Energi",
                    "maxlength": 150,
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": (
                        "Jelaskan masalah, tujuan, cara kerja, "
                        "komponen, dan manfaat proyekmu..."
                    ),
                    "rows": 6,
                }
            ),
            "category": forms.Select(),
            "status": forms.Select(),
            "collaboration_needs": forms.Textarea(
                attrs={
                    "placeholder": (
                        "Contoh: membutuhkan programmer ESP32, "
                        "teknisi elektronika, atau rekan penelitian..."
                    ),
                    "rows": 4,
                }
            ),
        }
