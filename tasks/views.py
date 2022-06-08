from django.shortcuts import render
from django.db.models import Q
from .models import Task, Comment

# Create your views here.

def profile_home(request):
    """ A view to return the index page """

    tasks = Task.objects.all()

    if request.GET:
        if 'months' in request.GET:
            months = request.GET['months']

            
            tasks = tasks.filter(end_date__month=months)

    context = {
        'tasks': tasks,
    }
    return render(request, 'tasks/profile_home.html', context)