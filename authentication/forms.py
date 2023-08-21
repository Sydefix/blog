from django import forms
from django.contrib.auth.forms import UserCreationForm as CreationForm
from .models import User

class UserCreationForm(CreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
