from django.contrib import admin
from django.urls import include, path

from frontend.urls import urlpatterns
from events.urls import router_v1


urlpatterns = [
    path('api/', include(router_v1.urls)),
    path('', include(urlpatterns)),
    path('admin/', admin.site.urls),
]
