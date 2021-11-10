from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import (
    HttpResponseRedirect,
    redirect,
    render,
    reverse
    
    )
from LsS.models import Post, Profilemodel
from LsS.forms import LoginForm, PostForm

"""Showing Posts here"""


def index(request):
    if request.user.is_authenticated:
        user = Profilemodel.objects.get(id=request.user.id)
        user.following.add(user)
        following = user.following.all()
        post = Post.objects.filter(profileuser__in=following)

        return render(request, "home.html", {"posts": post})
    else:
        return redirect("register")


"""Updating Profile View"""


def profile_upload(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user_bio = request.POST["bio"]
            profile_pic = request.FILES["file"]
            Profilemodel.objects.create(
                image=profile_pic, bio=user_bio, user=request.user
            )
            if profile_upload:
                return redirect("profile.html")
            else:
                return HttpResponse("Error! Please Try Again Later")
        return render(request, "edit_profile.html")
    else:
        return redirect("register")


"""Showing Profile """


def profile(request, id):
    if request.user.is_authenticated:
        profile = Profilemodel.objects.get(id=id)
        posts = Post.objects.filter(profileuser=profile)
        return render(request, "profile.html", {"profile": profile, "posts": posts})
    else:
        return redirect("/register/")


"""Sign Up And Redirecting to profile page """


def signup(request):
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        password = request.POST["password"]
        if Profilemodel.objects.filter(username=username).first():
            messages.warning(request, "Username already exists")
            return redirect("register")
        else:
            a = Profilemodel.objects.create_user(username, email, password)
            a.first_name = fname
            a.last_name = lname
            a.save()
            if a:
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("home")
    return render(request, "register.html", {})


"""For logout"""


def logout(request):

    return redirect("login")


"""Search """


def search(request):

    return render(request, "search.html")


"""Following user here"""


def follow_user(request):

    return redirect("search")


"""For logging Users"""


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", reverse("home")))
    form = LoginForm()
    return render(request, "login.html", {"form": form})


""" For Uploading Post"""


# @login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post = Post.objects.create(
                text=data['post'],
                profileuser=request.user
            )
        return redirect('/')
    form = PostForm()
    return render(request, 'post.html', {'form': form})


# def add_post(request):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             id = request.user.id
#             profile = Profilemodel.objects.get(id=id)
#             # postdesc = request.POST["desc"]
#             # file = request.FILES["file"]
#             Post.objects.create(
#                 post=post, user=profile
#             )
#         return render(request, "post.html")
#     else:
#         return redirect("register")
