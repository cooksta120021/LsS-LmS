from django.contrib import admin
from twitter_tweet.models import Tweet
from twitter_user.models import NewUser
from twitter_notification.models import Notification
# Register your models here.

admin.site.register(Tweet)
admin.site.register(NewUser)
admin.site.register(Notification)
