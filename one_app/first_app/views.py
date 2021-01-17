from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial
 
def homepage(request): 
   all_tasks = Tutorial.objects.all
   return render(request, 'homepage.html', {'all_tasks':all_tasks})


def delete_task(request):
    return render(request, 'homepage.html', {})

def complete_task(request):
    return render(request, 'homepage.html', {})

def pending_task(request):
    return render(request, 'homepage.html', {})

def edit_task(request):
    return render(request, 'edit.html', {})

def index(request):
   context = {
       'welcome_text':"welcome from index."
   }
   return render(request, 'index.html', context)
 
def about(request):
   context = {
       'welcome_text':"welcome from about."
   }
   return render(request, 'about.html', context)
 
def contact(request):
   context = {
       'welcome_text':"welcome from contact."
   }
   return render(request, 'contact.html', context)


def pricing(request):
   context = {
       'welcome_text':"welcome from contact."
   }
   return render(request, 'pricing.html', context)