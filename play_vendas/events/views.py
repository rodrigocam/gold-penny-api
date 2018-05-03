from rest_framework import viewsets
from .serializers import EventSerializer, ProductSerializer
from .models import Event, Product
from rest_framework.response import Response


class EventViewSet(viewsets.ModelViewSet):
    # queryset = Event.objects.all()
    # serializer_class = EventSerializer
    def list(self, request):
        queryset = Event.objects.filter(user = request.user)
        serializer = EventSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    #@TO-DO: update method to increase total_earnings

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    #@TO-DO: turn into read only, and verify authentication token