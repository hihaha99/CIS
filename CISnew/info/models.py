from django.db import models

class Stores(models.Model):
    name = models.CharField(max_length=200)
    wait_time = models.IntegerField()
    start_hour = models.TimeField(default="08:00:00")
    end_hour = models.TimeField(default="08:00:00")
    
    def __str__(self):
        return self.name

class Dishes(models.Model):
    store = models.ForeignKey(Stores,on_delete=models.CASCADE)
    dname = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2,max_digits=5)
    start_hour = models.TimeField(default="08:00:00")
    end_hour = models.TimeField(default="08:00:00")

    def __str__(self):
        return self.dname

