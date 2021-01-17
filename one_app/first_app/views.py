from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskList
 
# Create your views here.
def todolist(request): 
   all_tasks = TaskList.objects.all
   return render(request, 'todolist.html', {'all_tasks':all_tasks})


def delete_task(request):
    return render(request, 'todolist.html', {})

def complete_task(request):
    return render(request, 'todolist.html', {})

def pending_task(request):
    return render(request, 'todolist.html', {})

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