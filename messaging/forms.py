from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["body"]
        labels = {
            "body": "Pesan",
        }
        widgets = {
            "body": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "Tulis pesan kepada pengguna...",
                "maxlength": 5000,
            }),
        }

    def clean_body(self):
        body = self.cleaned_data["body"].strip()

        if not body:
            raise forms.ValidationError("Pesan tidak boleh kosong.")

        return body
