from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomCreationUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username',)

class CustomChangeUserForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)