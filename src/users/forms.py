from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    login_username = forms.CharField(label="Nombre de usuario")
    login_password = forms.CharField(label="Contraseña")


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label = "Nombre")
    last_name = forms.CharField(max_length=30, label = "Apeliidos")
    username = forms.CharField(max_length=30, required=True, label = "Nombre de usuario")
    email = forms.EmailField(max_length=254, required=True, label = "yourmail@yourmail.com")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'username', 'email', 'password1', 'password2',)
