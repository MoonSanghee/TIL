from django import forms
from .models import Infos
from django import forms

class InfosForm(forms.ModelForm):
    class Meta:
        model = Infos
        fields = '__all__'