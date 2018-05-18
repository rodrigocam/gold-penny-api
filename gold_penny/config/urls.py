from django.contrib import admin
from django.urls import include, path

from users.urls import urlpatterns as users_urlpatterns
from events.urls import router_v1


urlpatterns = [
    path('api/v1', include(router_v1.urls)),
    path('', include(users_urlpatterns)),
    path('admin/', admin.site.urls),
]
