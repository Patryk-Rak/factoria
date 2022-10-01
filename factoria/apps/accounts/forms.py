from django.forms import models
from django import forms
from .models import Client

class ListForm(models.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'

class LoginForm(models.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = Client
        fields = ('email', 'password')