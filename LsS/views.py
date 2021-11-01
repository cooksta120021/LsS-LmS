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
from LsS.models import User, Post
from django.shortcuts import (
    # HttpResponse, 
    HttpResponseRedirect, 
    # get_object_or_404, 
    render, 
    reverse
)
from LsS.forms import LoginForm, ProfileUpdateForm, SignUp


@login_required
def home_view(request):
    user = User.objects.all()
    return render(request, 'home.html', {'user':user})

@login_required
def post(request):
    context = {'post': Post.objects.all().order_by('-datetime'),
               }
    return render(request, 'home.html', context)


def user_profile_view(request, id):
    user = User.objects.get(id=id)
    return render(request, 'user_detail.html', {'profile': user})

def user_edit(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.about = data['about']
            user.save()
            return render(request, 'user_detail.html')
    form = ProfileUpdateForm()
    return render(request, 'edit_profile.html', {'form': form})

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


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))
