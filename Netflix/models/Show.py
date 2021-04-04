from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Producer(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Prize(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Show(models.Model):
    name = models.CharField(max_length=50)
    show_type = models.CharField(max_length=50)
    story = models.TextField()
    country = models.CharField(max_length=50)
    duration = models.DurationField()
    production_Date = models.DateField()
    rating = models.FloatField()
    classification = models.CharField(max_length=50)
    publish_Date = models.DateField()
    video_Source = models.URLField(max_length=200)
    poster = models.URLField(max_length=200)
    language = models.CharField(max_length=50)
    genres = models.ManyToManyField(Genre)
    directors = models.ManyToManyField(Director)
    authors = models.ManyToManyField(Author)
    producers = models.ManyToManyField(Producer)
    actors = models.ManyToManyField(Actor)
    prizes = models.ForeignKey(Prize,null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.name




