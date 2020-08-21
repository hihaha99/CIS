from django.contrib import admin
from .models import Stores ,Dishes , Review
# Register your models here.

admin.site.register(Stores)
admin.site.register(Dishes)
admin.site.register(Review)