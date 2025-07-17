from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

# Define data entities

class Book(models.Model):
    # Define the structure and its types of data (https://docs.djangoproject.com/en/5.2/ref/models/fields/)
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])  # Rating between 1 and 5
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True) # Harry Potter 1 => harry-potter-1
    
    # Define the URL to access the book detail page
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # Automatically create a slug from the title
        super().save(*args, **kwargs) # save the data to the database


    def __str__(self): # How the instances be output in the terminal
        return f"{self.title} ({self.rating})"