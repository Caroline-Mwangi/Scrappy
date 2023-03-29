from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('srchtag', views.srchtag, name="srchtag"),
    path('username', views.username, name="username"),
]