from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "scrapp/index.html")

def srchtag(request):
    return render(request, "scrapp/srch_tag.html")

def username(request):
    return render(request, "scrapp/username.html")
