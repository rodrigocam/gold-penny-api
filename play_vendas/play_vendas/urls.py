from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from rest_framework import routers
from event import views

router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns.append(
            path('__debug__/', include(debug_toolbar.urls))
        )
