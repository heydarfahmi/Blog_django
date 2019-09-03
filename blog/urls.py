from django.contrib import admin
from django.urls import path, include

from blog.views import base

urlpatterns = [
    path('',base)
]
