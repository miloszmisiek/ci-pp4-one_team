from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from tasks.views import ALL_USERS
from .models import CustomUser
from .forms import UserSignupForm, EditProfileForm

def edit_profile(request, user_id):
    current_user = request.user

    user = get_object_or_404(CustomUser, id=user_id)
    
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            obj = form.save(commit=False)
            if obj.rank != current_user.rank:
                obj.is_active = False
                obj.save()
                return HttpResponseRedirect("/accounts/inactive/")
            obj.save()
            return HttpResponseRedirect("/tasks/my_tasks/")
    else:
        form = EditProfileForm(instance=user)

    context = {
        "form": form,
    }
    return render(request, "users/edit_profile.html", context)

