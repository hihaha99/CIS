from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def info(request):
    return HttpResponse("Hello, world. You're at the info index.")