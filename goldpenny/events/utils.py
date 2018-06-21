from django.db import transaction
from .models import Product, Event


def sell_product(user, product_id, amount):
    with transaction.atomic():
        event = Event.objects.filter(user=user)[0]
        print(f'EVENT {event}')
        product = Product.objects.select_for_update().get(
            event=event,
            id=product_id
        )
        product.total_sold += amount
        print(f'PRODUCT {product}')
        product.save()
