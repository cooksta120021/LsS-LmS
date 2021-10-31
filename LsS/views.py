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
from LsS.forms import LoginForm

# Create your views here.

def home(request):
    user = User.objects.all()
    return render(request, 'home.html', {'user':user})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            users = authenticate(
                request, username=data.get("username"), password=data.get("password")
            )
            if users:
                login(request, users)
                return HttpResponseRedirect(
                    request.GET.get("next", reverse("home"))
                )

    form = LoginForm()
    return render(request, "login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))
