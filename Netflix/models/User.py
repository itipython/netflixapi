from django.db import models
from .Show import Show
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class Membership(models.Model):
    name = models.CharField(max_length=50)
    duration = models.IntegerField()
    price = models.CharField(max_length=50)
    Resolution = models.IntegerField()
    # Offers = 
    no_of_Active_Screens = models.IntegerField()


    def __str__(self):
        return self.name

# class User(models.Model):
#     firstName = models.CharField(max_length=50)
#     lastName = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     email = models.EmailField(max_length=254)
#     phone = models.CharField(max_length=50)
#     country	= models.CharField(max_length=100)
#     birth_date = models.DateField()
#     gender	= models.CharField(max_length=50)
#     register_Date = models.DateField()
#     avatar = models.URLField(max_length=200)
#     membership = models.ForeignKey(Membership,null=True, on_delete=models.SET_NULL)
#     payment_Day	= models.DateField()
#     membership_Start_Date = models.DateField()


    def __str__(self):
        return (f'{self.first_Name} {self.last_Name}')
    


class Watch(models.Model):
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    User_id	= models.ForeignKey(User, on_delete=models.CASCADE)
    Date = 	models.DateField()
    Current_Duration = models.DurationField()



class Watched(models.Model):
    Show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    User_id	= models.ForeignKey(User, on_delete=models.CASCADE)
    User_Rating = models.IntegerField() 



class WatchLater(models.Model):
    Show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    User_id	= models.ForeignKey(User, on_delete=models.CASCADE)



class Subscribe(models.Model):
    membership = models.ForeignKey(Membership,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    start_date = models.models.DateTimeField()
    payment_date = models.DateTimeField()