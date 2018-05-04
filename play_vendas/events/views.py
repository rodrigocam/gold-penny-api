from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Event, Product
from .serializers import EventSerializer, ProductSerializer


class EventViewSet(viewsets.ModelViewSet):

    def list(self, request):
        queryset = Event.objects.filter(user=request.user)
        serializer = EventSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def increase_total_earnings(self, request):
        event = Event.objects.get(user=request.user)
        event.total_earnings += 1
        event.save()
        serializer = EventSerializer(event)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):

    def list(self, request):
        event = Event.objects.get(user=request.user)
        products = event.products

        serializer = ProductSerializer(
            products,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)