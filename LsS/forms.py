from django import forms
from django.contrib.auth.forms import UserCreationForm

from LsS.models import User



class SignUp(forms.Form):
    username = forms.CharField( max_length=140)
    password = forms.CharField(widget=forms.PasswordInput)



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileUpdateForm(forms.Form):
    class Meta:
        model = User
        fields = ['image', 'bio']
