from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

from users.urls import urlpatterns as users_urlpatterns
from events.urls import router_v1


urlpatterns = [
    path('', include(users_urlpatterns)),
    path('api/v1/', include(router_v1.urls)),
    path('get-token/', views.obtain_auth_token),
    path('admin/', admin.site.urls),
]
