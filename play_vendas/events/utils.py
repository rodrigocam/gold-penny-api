from django.db import transaction
from .models import Product, Event


def sell_product(user, product_id, amount):
    with transaction.atomic():
        event = Event.objects.filter(user=user)[0]
        product = Product.objects.select_for_update().get(
            event=event,
            id=product_id
        )
        product.total_sold += amount
        product.save()
