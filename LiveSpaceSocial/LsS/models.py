from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class NewUser(AbstractUser):
    user = models.CharField(max_length=15, unique=True)
    image = models.ImageField(null=True, blank=True)
    follow = models.ManyToManyField('self', symmetrical=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username
