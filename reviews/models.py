from django.db import models

# Create your models here.

class Rating(models.Model):
    rating = models.CharField(max_length=50)
    rating_slug=models.SlugField()
    def get_absolute_url(self):
         return "/ratings/%s/" % self.rating_slug

class Category(models.Model):
    category = models.CharField(max_length=50)
    category_slug=models.SlugField()
    def get_absolute_url(self):
         return "/category/%s/" % self.category_slug

class Business(models.Model):
    name = models.CharField(max_length=255)
    name_slug=models.SlugField()
    rating=models.ForeignKey(Rating)
    category=models.ForeignKey(Category)

    
class Review(models.Model):
    name_of_business = models.ForeignKey(Business)
    description = models.TextField()
    rating=models.ForeignKey(Rating)
    reviewer=models.CharField(max_length=250)


