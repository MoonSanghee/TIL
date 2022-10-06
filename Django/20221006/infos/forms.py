from dataclasses import field
from django import forms
from .models import Infos

class InfosForm(forms.ModelForm):
    class Meta:
        model = Infos
        fields = '__all__'
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control mt-2",
                }
            ),
            "summary": forms.Textarea(attrs={"class": "form-control mt-2", "rows": 10}),
            "running_time": forms.TextInput(
                attrs={
                    "class": "form-control mt-2",
                }
            ),
        }
        labels = {
            "title": "제목",
            "summary": "줄거리",
            "running_time": "러닝 타임",
        }