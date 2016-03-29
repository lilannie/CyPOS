from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms


class UserForm (ModelForm):
    first_name = forms.CharField(help_text="First Name:")
    last_name = forms.CharField(help_text="Last Name:")
    username = forms.CharField(help_text="Username:")
    email = forms.CharField(help_text="Email:")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Password:")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


