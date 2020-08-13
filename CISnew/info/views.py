from django.shortcuts import render , redirect 
from datetime import datetime
from django.views.generic.edit import CreateView
# Create your views here.
from django.http import HttpResponse
from .models import Stores, Dishes 
from .forms import StoresForm, DishesForm ,CustomTime
from django.contrib import messages

def info(request):
    stores = Stores.objects.all()
    context={'stores':stores,"form":CustomTime()}
    return render(request,'info/index.html',context)

def add_store(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StoresForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            messages.success(request, f'Store added!')
            return redirect ("info")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StoresForm()

    return render(request, 'info/add_store.html', {'form': form})

def add_dish(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DishesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            messages.success(request, f'Dish added!')
            return redirect ("info")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DishesForm()

    return render(request, 'info/add_dish.html', {'form': form})

def current_store(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    stores=Stores.objects.filter(start_hour__lte=current_time, end_hour__gte=current_time)
    context={'stores':stores}
    return render(request,'info/current.html',context)

def custom_store(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CustomTime(request.POST)
    time=form['time'].value()
    current_time = time
    stores=Stores.objects.filter(start_hour__lte=current_time, end_hour__gte=current_time)
    context={'stores':stores}
    return render(request,'info/custom.html',context)