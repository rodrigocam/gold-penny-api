from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Event, Product
from .serializers import EventSerializer, ProductSerializer, SellSerializer
from .utils import sell_product


class EventViewSet(viewsets.ModelViewSet):

    def list(self, request):
        queryset = Event.objects.filter(user=request.user)
        serializer = EventSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Event.objects.filter(user=request.user)
        event = get_object_or_404(queryset, pk=pk)
        serializer = EventSerializer(event, context={'request': request})
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
        queryset = Product.objects.filter(request=request.user)
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    @action(methods=['post'], detail=False)
    def sell(self, request):
        print(f'REQUEST DATA {request.data}')
        serializer = SellSerializer(data=request.data)
        if serializer.is_valid():
            print(f'DATA {serializer.data}')
            orders = serializer.data['orders']
            print(f'ORDERS {orders}')
            for order in orders:
                print('ENTROU NO FOR')
                sell_product(request.user, order['id'], order['amount'])
        
            return Response('Successfully sold', status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)