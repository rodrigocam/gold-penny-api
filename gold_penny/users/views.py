from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect

from events.models import Event, Product
from users.forms import LoginForm


def index(request):
    if request.user.is_authenticated:
        total_earnings = 0
        products_sold = []

        event = list(Event.objects.filter(user=request.user))
        if event:
            event = event[0]
            products_sold = Product.objects.filter(event=event)
            for product in products_sold:
                total_earnings += product.price * product.total_sold

        ctx = {
            'event': event,
            'total_earnings': total_earnings,
            'products_sold': products_sold,
        }

        return render(request, 'users/home.jinja2', ctx)

    return HttpResponseRedirect('/login')
