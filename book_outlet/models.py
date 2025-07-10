from django.db import models

# Create your models here.

# Define data entities

class Book(models.Model):
    # Define the structure and its types of data (https://docs.djangoproject.com/en/5.2/ref/models/fields/)
    title = models.CharField(max_length=50)
    rating = models.IntegerField()