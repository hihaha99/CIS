from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Stores, Dishes


def info(request):
    stores = Stores.objects.all()
    context={'stores':stores}
    return render(request,'info/index.html',context)
