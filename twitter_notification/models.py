from twitter_tweet.models import Tweet
from django.db import models
from twitter_user.models import NewUser



class Notification(models.Model):
    post = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    sender = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='noti_from')
    reciever = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='noti_to')
    is_seen = models.BooleanField(default=False)
