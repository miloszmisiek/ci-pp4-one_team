from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Task
from .forms import AddTask
from django.contrib.auth.decorators import user_passes_test
from datetime import date, timedelta
from users.models import CustomUser

USER = get_user_model()
ALL_USERS = USER.objects.all()
MASTER_EXCLUDED = ALL_USERS.exclude(is_superuser=True)
TODAY = date.today()
YESTERDAY = TODAY - timedelta(days=1)
CLEAR_UPDATED = TODAY - timedelta(days=2)


@login_required(login_url="/accounts/login/")
def profile_home(request):
    """A view to return the tasks home page"""
    tasks = Task.objects.all().filter(assigned_to__is_active=True)

    tasks.filter(end_date__lt=TODAY, status=0).update(status=2)
    tasks.filter(end_date__gte=TODAY, status=2).update(status=0)

    tasks = tasks.exclude(Q(updated_on__lte=CLEAR_UPDATED) & Q(status=1))

    if request.GET and "months" in request.GET:
        months = request.GET["months"]
        tasks = tasks.filter(Q(created_on__month=months) | Q(end_date__month=months))

    if request.POST and "hide-completed" in request.POST:
        tasks = tasks.exclude(status=1)

    context = {
        "tasks": tasks,
    }
    return render(request, "tasks/profile_home.html", context)


@login_required(login_url="/accounts/login/")
def my_tasks(request):
    """A view to return the tasks home page"""
    tasks = Task.objects.all().filter(assigned_to=request.user)
    tasks.filter(end_date__lt=TODAY, status=0).update(status=2)
    tasks.filter(end_date__gte=TODAY, status=2).update(status=0)

    tasks = tasks.exclude(Q(updated_on=CLEAR_UPDATED) | Q(status=1))

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
    return render(request, "tasks/my_tasks.html", context)


@login_required(login_url="/accounts/login/")
def add_task(request):
    """A view to add tasks to database"""
    current_user = request.user
    if current_user.rank == 3:
        return render(request, "users/no_permission.html")
    else:
        if request.method == "POST":
            form = AddTask(request.POST, assigned_to=ALL_USERS)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.created_by = current_user
                if current_user.rank == 2:
                    obj.assigned_to = current_user
                    obj.save()
                elif current_user.rank == 1:
                    obj.approval_status = 2 if obj.priority != 0 else 1
                    obj.save()
                elif current_user.rank == 0:
                    obj.approval_status = 2
                    obj.save()
                else:
                    obj.save()
                return HttpResponseRedirect("/tasks/")
        else:
            if current_user.is_superuser:
                form = AddTask(
                    assigned_to=ALL_USERS, initial={"assigned_to": current_user.id}
                )
            elif current_user.rank == 2:
                form = AddTask(
                    assigned_to=ALL_USERS.filter(id=request.user.id),
                    initial={"assigned_to": current_user.id},
                )
            else:
                form = AddTask(
                    assigned_to=MASTER_EXCLUDED,
                    initial={"assigned_to": current_user.id},
                )

            context = {"form": form}

            return render(request, "tasks/add_task.html", context)


@login_required(login_url="/accounts/login/")
def edit_task(request, task_id):
    """A view to edit tasks in database"""
    task = get_object_or_404(Task, id=task_id)
    current_user = request.user
    if (
        current_user.rank == 3
        or current_user.rank == 2
        and task.assigned_to != current_user
        or task.assigned_to.rank == 0
        and not current_user.is_superuser
    ):
        return render(request, "users/no_permission.html")
    else:
        if request.method == "POST":
            form = AddTask(request.POST, assigned_to=ALL_USERS, instance=task)
            if form.is_valid():
                obj = form.save(commit=False)
                if current_user.rank == 2:
                    obj.assigned_to = current_user
                    obj.save()
                elif current_user.rank == 1:
                    obj.approval_status = 2 if obj.priority != 0 else 1
                    obj.save()
                else:
                    obj.save()
                return HttpResponseRedirect("/tasks/")
        else:
            if current_user.is_superuser:
                form = AddTask(
                    assigned_to=ALL_USERS,
                    instance=task,
                    initial={"assigned_to": current_user.id},
                )
            elif current_user.rank == 2:
                form = AddTask(
                    assigned_to=ALL_USERS.filter(id=request.user.id),
                    instance=task,
                    initial={"assigned_to": current_user.id},
                )
            else:
                form = AddTask(
                    assigned_to=MASTER_EXCLUDED,
                    instance=task,
                    initial={"assigned_to": current_user.id},
                )
    context = {
        "form": form,
    }
    return render(request, "tasks/edit_task.html", context)


@login_required(login_url="/accounts/login/")
def approve_task(request, task_id):
    """A view to approve tasks in the database"""
    task = get_object_or_404(Task, id=task_id)
    current_user = request.user
    if (
        current_user.rank == 3
        or current_user.rank == 2
        or current_user.rank == 1
        and task.priority == 0
        or task.assigned_to.rank == 0
        and not current_user.is_superuser
    ):
        return render(request, "users/no_permission.html")
    else:
        task.approval_status = 0 if task.approval_status == 1 else 1
        task.save()
        return redirect("tasks")


@login_required(login_url="/accounts/login/")
def complete_task(request, task_id):
    """A view to complete tasks in the database"""
    task = get_object_or_404(Task, id=task_id)
    current_user = request.user
    if (
        current_user.rank == 3
        or current_user.rank == 2
        and task.assigned_to != current_user
        or task.approval_status == 1
        or task.assigned_to.rank == 0
        and not current_user.is_superuser
    ):
        return render(request, "users/no_permission.html")
    else:
        task.status = 1 if task.status == 0 or task.status == 2 else 0
        task.save()
        return redirect("tasks")


@login_required(login_url="/accounts/login/")
def delete_task(request, task_id):
    """A view to delete tasks from database"""
    task = get_object_or_404(Task, id=task_id)
    current_user = request.user
    if (
        current_user.rank == 3
        or current_user.rank == 2
        and task.assigned_to != current_user
        or task.approval_status == 1
        and not current_user.is_superuser
        or task.assigned_to.rank == 0
        and not current_user.is_superuser
    ):
        return render(request, "users/no_permission.html")
    else:
        task.delete()
        return redirect("tasks")
