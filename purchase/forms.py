from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=50, required=True, help_text='Required.')
    telephone = forms.CharField(max_length=50, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'telephone', 'password1', 'password2')
