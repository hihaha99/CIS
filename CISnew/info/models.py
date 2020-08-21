from django.db import models
from django.contrib.auth.models import User

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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user.username} Profile'

"""     def save(self,*args,**kwargs):
        super().save(self,*args,**kwargs)
        img = Image.open(self.image.path)
        if img.height>300 or img.width >300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path) """

class Review(models.Model):
    store = models.ForeignKey(Stores,on_delete=models.CASCADE,related_name='review')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='review')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user.username)