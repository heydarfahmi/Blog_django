from django.contrib import admin
from django.urls import path, include

from blog.views import list_of_posts

urlpatterns = [
    path('', list_of_posts,name='listed_post'),
    path('tag/<tag_slug>', list_of_posts, name='listed_post_by_post'),

]
