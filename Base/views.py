from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
import re

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == "POST":
        print('post')

        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        number = request.POST.get('number')

        print(name, email, number, content)

        # Basic validations
        if not (2 < len(name) < 30):
            messages.error(request, 'Name should be between 2 and 30 characters.')
        elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            messages.error(request, 'Please enter a valid email address.')
        elif not re.match(r'^\d{10,13}$', number):
            messages.error(request, 'Please enter a valid phone number (10 to 13 digits).')
        elif not content or len(content.strip()) == 0:
            messages.error(request, 'Message content cannot be empty.')
        else:
            contact = Contact(name=name, email=email, content=content, number=number)
            contact.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('home')  # Optional: refreshes the page and clears the form

    return render(request, 'home.html')
