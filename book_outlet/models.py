from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

# Define data entities

# N:N with Book
class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)
    
    def __str__(self):
        return f"{self.name} ({self.code})"
    
    class Meta:
        verbose_name_plural = "Countries"


# 1:1 with Author
class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self): # How the instances be printed as Strings
        return f"{self.street}, {self.postal_code}, {self.city}"
    
    class Meta:
        verbose_name_plural = "Address Entries"  # Custom plural name for the model in admin panel

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self): # How the instances be printed as Strings
        return self.full_name()


class Book(models.Model):
    # Define the structure and its types of data (https://docs.djangoproject.com/en/5.2/ref/models/fields/)
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])  # Rating between 1 and 5
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books") # CASCADE: if the author is deleted, all books by that author will also be deleted
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) # Harry Potter 1 => harry-potter-1
    published_countries = models.ManyToManyField(Country, null=False, related_name="books")
    
    # Define the URL to access the book detail page
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)  # Automatically create a slug from the title
    #     super().save(*args, **kwargs) # save the data to the database


    def __str__(self): # How the instances be printed as Strings
        return f"{self.title} ({self.rating})"