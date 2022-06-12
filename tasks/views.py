from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Task, Comment
from .forms import AddTask

# Create your views here.

def profile_home(request):
    """ A view to return the tasks home page """

    # show_completed = True
    tasks = Task.objects.all()

    if request.GET:
        if 'months' in request.GET:
            months = request.GET['months']
            tasks = tasks.filter(created_on__month=months)
        if 'clear_completed' in request.GET:
            tasks = tasks.exclude(status=1)


    # if request.POST:
    #     show_completed = False

    # if not show_completed:
    #     tasks = tasks.exclude(status=1)

    context = { 
        'tasks': tasks,
        # 'show_completed':show_completed,
    }
    return render(request, 'tasks/profile_home.html', context)

@login_required(login_url="/accounts/login/")
def add_task(request):
    """ A view to add tasks to database """
    if request.method == "POST":
        form = AddTask(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tasks/')
    else:
        form = AddTask


    context = {
        'form': form
    }

    return render(request, "tasks/add_task.html", context)