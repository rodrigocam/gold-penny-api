from rest_framework import routers
from events import views


router_v1 = routers.DefaultRouter()

router_v1.register(
    r'events',
    views.EventViewSet,
    base_name='event'
)

router_v1.register(
    r'products',
    views.ProductViewSet,
    base_name='product')
