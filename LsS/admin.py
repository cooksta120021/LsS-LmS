from django.contrib import admin
from .models import Post,Profilemodel

# Register your models here.
@admin.register(Post)
class post(admin.ModelAdmin):
    list_display = ('id','user')

@admin.register(Profilemodel)
class Profile(admin.ModelAdmin):
    list_display = ('id','user')