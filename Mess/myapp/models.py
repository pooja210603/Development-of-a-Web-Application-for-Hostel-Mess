from django.db import models
# from profiles.models import Userprofile
from django.db.models.fields import BooleanField
from django.core.exceptions import ValidationError
# makemigrations - create changes and store in  a file
# migrate - apply the pending changes created by makemigrations
# Create your models here.

class Suggest(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    suggestion=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
  
    
class MenuItem(models.Model):
    breakfast_foodlist= models.TextField(default='default_value')
    breakfast_ingredients = models.TextField(default='default_value')
    lunch_foodlist= models.TextField(default='default_value')
    lunch_ingredients = models.TextField(default='default_value')
    snacks_foodlist=models.TextField(default='default_value')
    snacks_ingredients = models.TextField(default='default_value')
    dinner_foodlist= models.TextField(default='default_value')
    dinner_ingredients =models.TextField(default='default_value')
    

from django.db import models

class Feedback(models.Model):
    # item = models.CharField(max_length=100, default='default_value_here')
    rating_choices = (
        ('1', '1 - Poor'),
        ('2', '2 - Fair'),
        ('3', '3 - Average'),
        ('4', '4 - Good'),
        ('5', '5 - Excellent'),
    )
    rating_food_quality = models.CharField(max_length=2, choices=rating_choices, default='3')
    rating_nutrients = models.CharField(max_length=2, choices=rating_choices, default='3')
    rating_hygiene = models.CharField(max_length=2, choices=rating_choices, default='3')
    created_at = models.DateTimeField(auto_now_add=True)
    