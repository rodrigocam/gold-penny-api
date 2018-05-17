from django.shortcuts import render
from django.contrib.auth import authenticate

def index(request):
    user = authenticate(request.user)
    event = 'Vila Mix'
    total_earnings = 250.00
    products = ['Cerveja', 'Vodka', 'Whisky']
    ctx = {'event': event, 'total_earnings': total_earnings, 'products': products}

    #if user:
    return render(request, 'frontend/home.jinja2', ctx)

    #return render(request, 'frontend/login.jinja2')
