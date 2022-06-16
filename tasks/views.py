from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Task
from .forms import AddTask
from django.contrib.auth.decorators import user_passes_test

USER = get_user_model()
ALL_USERS = USER.objects.all()
MASTER_EXCLUDED = ALL_USERS.exclude(is_superuser=True)


def is_not_bosun(user):
    return user.rank != 3


def profile_home(request):
    """A view to return the tasks home page"""
    tasks = Task.objects.all()

    if request.GET and "months" in request.GET:
        months = request.GET["months"]
        tasks = tasks.filter(Q(created_on__month=months) | Q(end_date__month=months))

    tasks = (
        tasks.exclude(status=1)
        if request.POST and "clear-completed" in request.POST
        else tasks
    )

    context = {
        "tasks": tasks,
    }
    return render(request, "tasks/profile_home.html", context)


@login_required(login_url="/accounts/login/")
@user_passes_test(is_not_bosun, login_url="tasks")
def add_task(request):
    """A view to add tasks to database"""
    current_user = request.user

    if request.method == "POST":
        form = AddTask(request.POST, assigned_to=ALL_USERS)
        if form.is_valid():
            if current_user.rank == 2:
                obj = form.save(commit=False)
                obj.assigned_to = current_user
                obj.save()
            elif current_user.rank == 1:
                obj = form.save(commit=False)
                if obj.priority != 0:
                    obj.approval_status = 2
                    obj.save()
            else:
                form.save()
            return HttpResponseRedirect("/tasks/")
    else:
        form = (
            AddTask(
                assigned_to=MASTER_EXCLUDED, initial={"assigned_to": current_user.id}
            )
            if not current_user.is_superuser
            else AddTask(
                assigned_to=ALL_USERS, initial={"assigned_to": current_user.id}
            )
        )

        form.fields["assigned_to"].disabled = True if current_user.rank == 2 else False

    context = {"form": form}

    return render(request, "tasks/add_task.html", context)


@login_required(login_url="/accounts/login/")
def edit_task(request, task_id):
    """A view to edit tasks in database"""
    task = get_object_or_404(Task, id=task_id)
    current_user = request.user
    if request.method == "POST":
        form = AddTask(request.POST, assigned_to=ALL_USERS, instance=task)
        if form.is_valid():
            if current_user.rank == 2:
                obj = form.save(commit=False)
                obj.assigned_to = current_user
                obj.save()
            elif current_user.rank == 1:
                obj = form.save(commit=False)
                obj.approval_status = 2 if obj.priority != 0 else 1
                obj.save()
            else:
                form.save()
            return HttpResponseRedirect("/tasks/")
    else:
        form = (
            AddTask(assigned_to=MASTER_EXCLUDED, instance=task)
            if not current_user.is_superuser
            else AddTask(
                assigned_to=ALL_USERS, initial={"assigned_to": current_user.id}
            )
        )

        form.fields["assigned_to"].disabled = True if current_user.rank == 2 else False

    context = {
        "form": form,
    }
    return render(request, "tasks/edit_task.html", context)


@login_required(login_url="/accounts/login/")
def approve_task(request, task_id):
    """A view to approve tasks in the database"""
    task = get_object_or_404(Task, id=task_id)
    task.approval_status = 0
    task.save()
    return redirect("tasks")

@login_required(login_url="/accounts/login/")
def complete_task(request, task_id):
    """A view to complete tasks in the database"""
    task = get_object_or_404(Task, id=task_id)
    task.status = 1 if task.status == 0 else 0
    task.save()
    return redirect("tasks")

@login_required(login_url="/accounts/login/")
def delete_task(request, task_id):
    """A view to delete tasks from database"""
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("tasks")
