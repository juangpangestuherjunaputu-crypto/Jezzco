from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile

        fields = [
            "full_name",
            "headline",
            "about",
            "interests",
            "skills",
            "education",
            "goal",
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={
                "placeholder": "Masukkan nama lengkap",
            }),

            "headline": forms.TextInput(attrs={
                "placeholder": "Contoh: Pengembang Teknologi",
            }),

            "about": forms.Textarea(attrs={
                "rows": 5,
                "placeholder": "Ceritakan dirimu, minat, dan ambisimu",
            }),

            "interests": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "Contoh: teknologi, bisnis, robotika",
            }),

            "skills": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "Contoh: Python, elektronika, desain",
            }),

            "education": forms.TextInput(attrs={
                "placeholder": "Contoh: SMK Mekatronika",
            }),

            "goal": forms.Select(),
        }