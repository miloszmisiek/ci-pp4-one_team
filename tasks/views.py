from django.shortcuts import render

# Create your views here.

def profile_home(request):
    """ A view to return the index page """
    return render(request, 'tasks/profile_home.html')