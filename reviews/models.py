from django.db import models

# Create your models here.

class RestaurantType(models.Model):
    restaurant_type=models.CharField(max_length=255)
    restaurant_slug=models.SlugField()
    def get_absolute_url(self):
         return "/types/%s/" % self.restaurant_slug
    def __unicode__(self):
        return self.restaurant_type

class Category(models.Model):
    category = models.CharField(max_length=50)
    category_slug=models.SlugField()
    class Meta:
        verbose_name_plural="categories"
    def get_absolute_url(self):
         return "/category/%s/" % self.category_slug
    def __unicode__(self):
        return self.category

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    name_slug=models.SlugField()
    description=models.TextField()
    location=models.CharField(max_length=255)
    restaurant_type=models.ManyToManyField(RestaurantType)
    category=models.ManyToManyField(Category)
    def get_absolute_url(self):
         return "/restaurant/%s/" % self.name_slug
    def __unicode__(self):
        return self.name

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    reviewer=models.CharField(max_length=255)
    review=models.TextField()
    rating=models.FloatField()
    pubdate=models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
         return "/review/%i/" % self.id
    def __unicode__(self):
        return self.restaurant.name
