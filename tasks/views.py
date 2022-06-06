from django.shortcuts import render
from .models import Task, Comment

# Create your views here.

def profile_home(request):
    """ A view to return the index page """

    tasks = Task.objects.all()

    context = {
        'tasks': tasks,
    }
    return render(request, 'tasks/profile_home.html', context)