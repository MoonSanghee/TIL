from dataclasses import fields
from django import forms
from django import forms
from .models import Reviews

class sppForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = '__all__'