from django.shortcuts import render
from django.contrib.auth import authenticate

def index(request):
    user = authenticate(request.user)

    if user:
        return render(request, 'frontend/home.jinja2')

    return render(request, 'frontend/login.jinja2')
