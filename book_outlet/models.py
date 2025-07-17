from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# Define data entities

class Book(models.Model):
    # Define the structure and its types of data (https://docs.djangoproject.com/en/5.2/ref/models/fields/)
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])  # Rating between 1 and 5
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    
    def __str__(self): # How the instances be output in the terminal
        return f"{self.title} ({self.rating})"