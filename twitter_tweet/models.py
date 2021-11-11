from twitter_user.models import NewUser
from django.db import models
from django.utils import timezone



class Tweet(models.Model):
    text = models.TextField(max_length=140, default='')
    name = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now)
