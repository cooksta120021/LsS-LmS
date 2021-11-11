from twitter_notification.models import Notification
from twitter_user.models import NewUser
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from twitter_tweet.models import Tweet
from twitter_tweet.forms import TweetForm
from django.shortcuts import redirect, render
import re


@login_required
def tweet(request):
    context = {'tweets': Tweet.objects.all().order_by('-datetime'),
               }
    return render(request, 'home.html', context)


@login_required
def add_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweets = Tweet.objects.create(
                text=data['text'],
                name=request.user,
            )
            pattern = re.compile(r'@(\w{1,15})')
            pattern_matches = pattern.findall(data['text'])
            if pattern_matches:
                for string in pattern_matches:
                    name = NewUser.objects.get(username=string)

                    # users_mentioned = NewUser.objects.filter(username__in=pattern_matches)
                    # for person in users_mentioned:
                    #     if person.username in pattern_matches:
                    # print(person.username, type(person))
                    notification = Notification.objects.create(
                        reciever=name,
                        sender=request.user,
                        post=tweets,
                    )
                return redirect('/')
    form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})


def view_tweet(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, 'tweet_detail.html', {'tweet': tweet})


@login_required
def deleteItem(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    tweet.delete()
    return HttpResponseRedirect('/')
