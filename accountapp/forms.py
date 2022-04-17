from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    
    #Quitamos mensajes de ayuda
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = { k: "" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

    #Quitamos mensajes de ayuda
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class UserAvatarForm(forms.Form):
    image = forms.ImageField()
