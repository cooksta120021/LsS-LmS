from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class Profilemodel(AbstractUser):
    image = models.ImageField(upload_to="ProfilePics", default='media/ProfilePics/thumb_15951118880user.png')
    bio = models.CharField(max_length=200)
    followers = models.ManyToManyField(
        'self', related_name="followers", blank=True, null=True
    )
    following = models.ManyToManyField('self', blank=True, null=True)


class Post(models.Model):
    text = models.CharField(max_length=140)
    profileuser = models.ForeignKey(
        Profilemodel, related_name="profile", on_delete=models.CASCADE
    )
    likes = models.ManyToManyField('self', related_name="likes", blank=True, null=True)
