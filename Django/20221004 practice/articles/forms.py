from django import forms
from django import forms
from .models import Articles

class ArticlesForm(forms.ModelForm):

    class Meta:
        model = Articles
        fields = '__all__'