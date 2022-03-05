from django.contrib import messages
from django.shortcuts import render
from .models import Contact
# Create your views here.
# function to acess the homepage

def home(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        terms=request.POST.get('terms')

        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.terms=terms

        messages.success(request,"messages sent successfully")
        return render(request,"home.html")

    else:
        return render(request,"home.html")
