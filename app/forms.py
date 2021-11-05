from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from app.models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']

class ShowForm(ModelForm):
    class Meta:
        model = Show 
        fields = '__all__'