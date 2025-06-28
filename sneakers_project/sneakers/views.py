from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Sneaker, Category
from .serializers import SneakerSerializer, CategorySerializer


class LatestSneakersList(APIView):
    def get(self, request, format=None):
        sneakers = Sneaker.objects.all()[0:4]
        serializer = SneakerSerializer(sneakers, many=True)
        return Response(serializer.data)
