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
class Profile(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=255)
    country	= models.CharField(max_length=100)
    birth_date = models.DateField()
    gender	= models.CharField(max_length=50)
    register_date = models.DateField(auto_now_add=True)
    avatar = models.TextField(null=True)
    membership = models.ForeignKey(Membership,null=True, on_delete=models.SET_NULL)
    payment_day	= models.IntegerField()
    membership_Start_Date = models.DateField()

    #  REQUIRED_FIELDS to create super user, They must not be null
    REQUIRED_FIELDS  = ["first_name","phone","country","birth_date","gender"    
                        ,"payment_day","membership_Start_Date",]

    def __str__(self):
        return (self.username)    




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