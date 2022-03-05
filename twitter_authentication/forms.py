from django import forms


class LoginForm(forms.Form):
    username = forms.CharField( max_length=140)
    password = forms.CharField(widget=forms.PasswordInput)
    
class SignUp(forms.Form):
    username = forms.CharField( max_length=140)
    password = forms.CharField(widget=forms.PasswordInput)
