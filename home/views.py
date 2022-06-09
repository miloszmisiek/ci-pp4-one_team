from django.shortcuts import render, redirect
from tasks.views import profile_home
# Create your views here.

def index(request):
    """ A view to return the index page """
    return profile_home(request) if request.user.is_authenticated else render(request, 'home/index.html')