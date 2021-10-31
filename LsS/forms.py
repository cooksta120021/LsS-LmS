from django import forms
from django.contrib.auth.forms import UserCreationForm

from LsS.models import User



class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileUpdateForm(forms.Form):
    class Meta:
        model = User
        fields = ['image', 'bio']
