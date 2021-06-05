from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User        
# Create your models here.
class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    website = models.URLField(max_length=100)

def __str__(self):
    return self.name    


class WatchList(models.Model):
    title = models.CharField(max_length=100)
    storyline = models.CharField(max_length=100)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title
    
class Review(models.Model):
    review_user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=100,null=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating) + " " + self.watchlist.title



# class Language(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Framework(models.Model):
#     name = models.CharField(max_length=50)
#     language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='framework')

#     def__str_(self):
#     return self.name



  
# class Movie(models.Model):
#     name = models.CharField(max_length=100)
#     descriptions = models.CharField(max_length=200)
#     active = models.BooleanField(default=True)

# def __self__(self):
#     return self.name

# class StreamPlatform(models.Model):
#     id = models.IntegerField(max_lenght=50)
#     name = models.CharField(max_length=100)
#     website = models.URLField(max_length=100)
#     about = models.CharField(max_length=100)

#     def __self__(self):
#         return self.name

# class WatchList(models.Model):
#     id = models.IntegerField(max_length=50)
#     title = models.CharField(max_length=100)        
#     director = models.CharField(max_length=100)
#     platform = models.ForeignKey(StreamPlatform, ondelete=models.CASCADE, related_name='watchlist')
#     created  = models.DateTimeField(auto_now_add=True)