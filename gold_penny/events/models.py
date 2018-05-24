from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    """
    Representation of a product on the system,
    can be anything that will be sold.
    """

    event = models.ForeignKey(
        'Event',
        related_name='products',
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        _('Name'),
        max_length=70,
        blank=False,
    )

    price = models.FloatField(
        _('Price'),
    )

    total_sold = models.BigIntegerField(
        _('Total Sold'),
        default=0,
    )

    def __str__(self):
        return self.name


class Event(models.Model):
    """
    Representation of a event (an occasion where
    products are going to be sold) on the system.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    name = models.CharField(
        _('Name'),
        max_length=50,
        blank=False,
    )

    date = models.DateField(
        _('Date'),
    )

    total_earnings = models.FloatField(
        _('Total Earnings'),
        default=0,
    )

    def __str__(self):
        return self.name
