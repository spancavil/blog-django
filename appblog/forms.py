from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm (forms.Form):
    title = forms.CharField(max_length=300)
    subtitle = forms.CharField(max_length=400)
    image = forms.ImageField()
    content = forms.CharField(max_length=4000, widget=forms.Textarea(attrs={"rows": 12}))
    author = forms.CharField(max_length=100)

class PostSearchForm (forms.Form):
    title = forms.CharField(max_length=100)

class ChatForm (forms.Form):
    chat = forms.CharField(max_length=400)
