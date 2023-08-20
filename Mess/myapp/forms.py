from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MenuItem



class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['breakfast_foodlist', 'breakfast_ingredients', 'lunch_foodlist', 'lunch_ingredients','snacks_foodlist', 'snacks_ingredients','dinner_foodlist', 'dinner_ingredients']


from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        # fields = ['item', 'rating']
        fields = ['rating_food_quality','rating_nutrients','rating_hygiene']