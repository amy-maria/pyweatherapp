# from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.conf import settings


def homepage(request):
    # return HttpResponse("Hello World. from Django")
    return render(request, "home.html")


def about(request):
    # return HttpResponse("about page")
    return render(request, "about.html")
