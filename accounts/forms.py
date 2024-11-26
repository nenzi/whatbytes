from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from accounts.models import CustomUser


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Email or Username")


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]
