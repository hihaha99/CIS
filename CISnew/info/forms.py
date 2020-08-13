from django import forms
from django.forms import ModelForm
from .models import Stores,Dishes
class StoresForm(ModelForm):
    class Meta:
        model = Stores
        fields = ['name', 'wait_time', 'start_hour', 'end_hour']
    # name = forms.CharField(max_length=200)
    # wait_time = forms.IntegerField()
    # start_hour = forms.TimeField()
    # end_hour = forms.TimeField()
    


        # widgets = {
        #     'name': forms.TextInput(attrs={'placeholder': 'Name'}),
        #     'description': forms.Textarea(
        #         attrs={'placeholder': 'Enter description here'}),

class DishesForm(ModelForm):
    class Meta:
        model = Dishes
        fields = ['store', 'dname', 'start_hour', 'end_hour','price']
        labels = {
        "dname": "Dish name"
    }

class CustomTime(forms.Form): 
    time = forms.TimeField() 