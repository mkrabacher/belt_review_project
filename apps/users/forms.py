from __future__ import unicode_literals
from django.db import models
from .models import User
from django import forms
from datetime import *

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255, min_length=4)
    first_name = forms.CharField(max_length=255, min_length=2)
    last_name = forms.CharField(max_length=255, min_length=2)
    email = forms.EmailField()
    birthday = forms.DateField()
    password = forms.CharField(max_length=100, min_length=8, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100, min_length=8, widget=forms.PasswordInput)

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)