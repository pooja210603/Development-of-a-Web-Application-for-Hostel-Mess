from django.shortcuts import render,HttpResponse
from datetime import datetime
from myapp.models import Suggest
from myapp.models import MenuItem
from django.contrib import messages
from myapp.forms import MenuItemForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# from .forms import CreateUserForm
from django.shortcuts import render
from .models import MenuItem

# Create your views here.
def index(request):
    return render(request,'index.html')
def menuweb(request):
    return render(request,'menuweb.html')
from django.core.exceptions import ValidationError
from django.shortcuts import render

from django.core.exceptions import ValidationError
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
def validate_name(value):
    if len(value) < 3:
        raise ValidationError('Name must be at least 3 characters long.')
    if any(char.isdigit() for char in value):
        raise ValidationError('Name cannot have numeric values.')
    if any(char in special_chars for char in value):
        raise ValidationError('Name cannot have special characters.')

def suggest(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            # Validate the name field
            validate_name(name)
            email=request.POST.get('email')
            suggestion=request.POST.get('suggestion')
            suggestion= Suggest(name=name,email=email,suggestion=suggestion,date=datetime.today())
            suggestion.save()
            messages.success(request, ' Suggestion Sent Successfully !')
            return render(request,'suggest.html')
        except ValidationError as e:
                error_message = e.message
                context = {'error_message': error_message}
                special_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
                if len(name) < 3:
                    messages.info(request, ' Name must be at least 3 characters long !')
                if any(char.isdigit() for char in name):
                    messages.info(request, ' Name cannot have numeric values !')
                if len(name) == 0:
                    messages.info(request, ' Name cannot be empty values !')                
                if any(char in special_chars for char in name):
                    messages.info(request, ' Name cannot have special characters!')  
                return render(request, 'suggest.html', context)
    else:
        return render(request, 'suggest.html')

def menu(request):
    menu_items = MenuItem.objects.all()
    form = MenuItemForm()
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')
    context = {'menu_items': menu_items, 'form': form}
    return render(request, 'menu.html', context)
def report(request):
    return render(request,'report.html')

def menuweb(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})


from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Save form data to database or perform other processing
            form.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect('feedback_success')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def feedback_success(request):
    return render(request, 'feedback_success.html')