from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from twitter_authentication.forms import LoginForm, SignUp
from twitter_user.models import NewUser

# Create your views here.


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('home')))
    form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def signup_view(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            NewUser.objects.create_user(
                username=data['username'],
                password=data['password'])
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
            return HttpResponseRedirect('/')
    form = SignUp()
    return render(request, 'register.html', {'form': form})
