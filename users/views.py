from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .models import CustomUser
from .forms import EditProfileForm
from allauth.account.views import PasswordChangeView
from django.urls import reverse


@login_required(login_url="/accounts/login/")
def edit_profile(request, user_id):
    current_user = request.user

    user = get_object_or_404(CustomUser, id=user_id)

    if current_user.id == user.id or current_user.is_superuser:
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
    else:
        return render(request, "users/no_permission.html")

    context = {
        "form": form,
    }
    return render(request, "users/edit_profile.html", context)


@login_required(login_url="/accounts/login/")
def delete_profile(request, user_id):
    """A view to delete user from database"""
    current_user = request.user
    user = get_object_or_404(CustomUser, id=user_id)
    if current_user.id == user.id or current_user.is_superuser:
        user.delete()
        return redirect("home")
    else:
        return render(request, "users/no_permission.html")


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    def get_success_url(self):
        success_url = reverse("edit_profile", kwargs={"user_id": self.request.user.id})
        return success_url
