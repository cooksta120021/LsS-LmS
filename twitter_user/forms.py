from django import forms
from django.db.models import fields
from twitter_user.models import NewUser
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = NewUser
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.Form):
    class Meta:
        model = NewUser
        fields = ['image', 'bio']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)