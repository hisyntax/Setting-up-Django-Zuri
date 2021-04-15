from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homePage(request):
    return HttpResponse("<h1>This is my first Django App.</>")
