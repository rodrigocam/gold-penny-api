from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from events.urls import router_v1


urlpatterns = [
    path('api/', include(router_v1.urls)),
    path('admin/', admin.site.urls),
]
