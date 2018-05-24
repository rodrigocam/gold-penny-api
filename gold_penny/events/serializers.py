from .models import Event, Product
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'url', 'name', 'date', 'products', 'total_earnings')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'url', 'name', 'price', 'event', 'total_sold')


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(max_value=None, min_value=0)
    amount = serializers.IntegerField(max_value=None, min_value=1)


class SellSerializer(serializers.Serializer):
    orders = OrderSerializer(many=True)
