from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from twitter_notification.models import Notification
from twitter_tweet.models import Tweet
from twitter_user.models import NewUser



@login_required
def index(request):
    users = NewUser.objects.all()
    cuser = request.user
    followed = cuser.following.all()
    tweets = Tweet.objects.all().order_by('-datetime')
    notifications = Notification.objects.filter(reciever=request.user, is_seen=False)
    return render (request, 'home.html', {'tweets':tweets, 'user': cuser, 'notifications':notifications, 'followed': followed, 'users':users})

def user_detail(request, user_id):
    cuser = NewUser.objects.get(id=user_id)
    tweets = Tweet.objects.filter(name=cuser)
    following = cuser.following.all()
    return render(request, 'profile.html', {'user': cuser, 'tweets': tweets, 'following': following})

def profile(request, user_id):
    profile = NewUser.objects.get(id=user_id)
    return render(request, 'profile.html', {'profile': profile})

def follow_view(request, author_id):
    usertofollow = NewUser.objects.get(id=author_id)
    cuser = request.user
    cuser.following.add(usertofollow)
    print(cuser.following)
    return redirect('/', author_id=request.user.id)


def unfollow_view(request, author_id):
    unfollow = NewUser.objects.get(id=author_id)
    cuser = request.user
    cuser.following.remove(unfollow)
    print(cuser.following)
    return redirect('/', author_id=request.user.id)

