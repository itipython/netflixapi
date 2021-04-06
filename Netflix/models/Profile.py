from django.contrib.auth.models import AbstractUser
from django.db import models
from .Show import Show
from django.contrib.auth.models import User

# Create your models here.

class Membership(models.Model):
    name = models.CharField(max_length=50)
    duration = models.IntegerField()
    price = models.CharField(max_length=50)
    Resolution = models.IntegerField()
    no_of_Active_Screens = models.IntegerField()


    def __str__(self):
        return self.name

# class User(models.Model):
class Profile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField(max_length=255)
    country	= models.CharField(max_length=100)
    birth_date = models.DateField()
    gender	= models.CharField(max_length=50)
    register_date = models.DateField()
    avatar = models.TextField()
    # membership = models.ForeignKey(Membership,null=True, on_delete=models.SET_NULL)
    payment	= models.DateField()
    membership_Start_Date = models.DateField()


    def __str__(self):
        return (f'{self.first_name} {self.last_name}')
    


class Watch(models.Model):
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    User_id	= models.ForeignKey(Profile, on_delete=models.CASCADE)
    Date = 	models.DateField()
    Current_Duration = models.DurationField()



class Watched(models.Model):
    Show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    User_id	= models.ForeignKey(Profile, on_delete=models.CASCADE)
    User_Rating = models.IntegerField() 



class WatchLater(models.Model):
    Show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    User_id	= models.ForeignKey(Profile, on_delete=models.CASCADE)



class Subscribe(models.Model):
    membership = models.ForeignKey(Membership,on_delete=models.CASCADE)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    payment_date = models.DateTimeField()