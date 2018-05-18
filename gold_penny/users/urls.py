from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import index


urlpatterns = [
    path('home/', index, name='home'),
    path('login/', auth_views.login, {'template_name': 'users/login.jinja2'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/home'}, name='logout')
]
