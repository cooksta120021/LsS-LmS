from django.contrib.auth import (
    authenticate, 
    login, 
    logout
    )
from django.contrib.auth.decorators import (
    login_required, 
    # permission_required, 
    # user_passes_test
    )
from LsS.models import User
from django.shortcuts import (
    # HttpResponse, 
    HttpResponseRedirect, 
    # get_object_or_404, 
    render, 
    reverse
)
from LsS.forms import LoginForm, SignUp

# Create your views here.

def home(request):
    user = User.objects.all()
    return render(request, 'home.html', {'user':user})



def signup_view(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(
                username=data['username'],
                password=data['password'])
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
            return HttpResponseRedirect('/')
    form = SignUp()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "GET":
        form = LoginForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request,'home.html')
    form = LoginForm()
    return render(request, "login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))
