from django import forms
from django.forms import fields
from LsS.models import Profilemodel


# class SignUp(forms.ModelForm):
#     class Meta:
#         model = Profilemodel
#         fields = [
#             'username','email','password'
#             ]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class PostForm(forms.Form):
    post = forms.CharField(max_length=140)
