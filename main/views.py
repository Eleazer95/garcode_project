# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from .models import ContactMessage

def test_view(request):
    return HttpResponse("Test view is working!")

def index(request):
    print("Index view called")
    return render(request, 'main/index.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the contact message to the database
            return redirect('main:contact_success')  # Redirect to success page
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'main/contact_success.html')

def services(request):
    return render(request, 'main/services.html')

def about(request):
    return render(request, 'main/about.html')
