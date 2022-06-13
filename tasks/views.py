from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Task, Comment
from .forms import AddTask

# Create your views here.

def profile_home(request):
    """ A view to return the tasks home page """
    tasks = Task.objects.all()

    if request.GET:
        if 'months' in request.GET:
            months = request.GET['months']
            tasks = tasks.filter(created_on__month=months)

    if request.POST:
        tasks = tasks.exclude(status=1)


    context = { 
        'tasks': tasks,
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

@login_required(login_url="/accounts/login/")
def edit_task(request, task_id):
    """ A view to edit tasks in database """
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = AddTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tasks/')
    form = AddTask(instance=task)
    context ={
        'form' : form,
    }
    return render(request, 'tasks/edit_task.html', context)

@login_required(login_url="/accounts/login/")
def delete_task(request, task_id):
    """ A view to delete tasks from database """
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks')