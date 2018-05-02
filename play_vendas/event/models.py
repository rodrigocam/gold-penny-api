from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=70, blank=False)
    price = models.FloatField()
    event = models.ForeignKey(
        'Event',
        related_name='products',
        on_delete=models.CASCADE
        )

class Event(models.Model):
    name = models.CharField(max_length=50, blank=False)
    date = models.DateField()