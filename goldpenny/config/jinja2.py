from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from jinja2 import Environment

from babel.numbers import format_currency


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    env.filters['currency'] = currency
    return env


def currency(value):
    return format_currency(value, 'BRL', locale='pt_BR')

