from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('index2', views.index2, name="index2"),
    path('tw_login', views.tw_login, name="tw_login"),
    path('srchtag', views.srchtag, name="srchtag"),
    path('username', views.username, name="username"),
]