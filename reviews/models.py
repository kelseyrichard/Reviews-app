from django.db import models

# Create your models here.

class place(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

class reviews(models.Model):
    description = models.CharField(max_length=1000)
   
