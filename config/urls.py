"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitter_tweet import views as tweet_views
from twitter_user import views as user_views
from twitter_notification import views as noti_views
from twitter_authentication import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', user_views.index, name='home'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view),
    path('register/', auth_views.signup_view, name='register'),
    path('addtweet/', tweet_views.add_tweet),
    path('singletweet/<int:tweet_id>/', tweet_views.view_tweet),
    path('user/<int:user_id>/', user_views.user_detail, name='userdetail'),
    path('profile/', user_views.profile, name='profile'),
    path('follow/<int:author_id>/', user_views.follow_view),
    path('unfollow/<int:author_id>/', user_views.unfollow_view),
    path('notification/', noti_views.notification_view),
    path('delete/<int:tweet_id>/', tweet_views.deleteItem, name='delete-item'),

]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', tweet_views.tweet, name='home'),
#     path("login/", auth_views.LoginView.as_view(template_name='login.html'), name='login'),
#     path('delete/<int:tweet_id>/', tweet_views.deleteItem, name='delete-item'),
#     path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
#     path('register/', user_views.register, name='register'),
#     path('profile/<int:user_id>/', user_views.profile, name='profile'),
#     path('profile_update/<int:profile_id',
#          user_views.profile_update, name='profile_update'),
#     path('add_tweet/', tweet_views.add_tweet, name='add_tweet'),
#     path('tweet_detail/<int:tweet_id>/',
#          tweet_views.view_tweet, name='add_tweet'),
#     path('follow/<int:follow_id>/', user_views.follow, name='like'),
#     path('unfollow/<int:unfollow_id>/', user_views.unfollow, name='dislike'),
# ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
