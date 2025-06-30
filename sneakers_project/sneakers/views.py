from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Sneaker, Category
from .serializers import SneakerSerializer, CategorySerializer


class LatestSneakersList(APIView):
    def get(self, request, format=None):
        sneakers = Sneaker.objects.all()[0:4]
        serializer = SneakerSerializer(sneakers, many=True)
        return Response(serializer.data)


class SneakerDetail(APIView):
    def get_object(self, category_slug, sneaker_slug):
        try:
            return Sneaker.objects.filter(category__slug=category_slug).get(
                slug=sneaker_slug
            )
        except Sneaker.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, sneaker_slug, format=None):
        sneaker = self.get_object(category_slug, sneaker_slug)
        serializer = SneakerSerializer(sneaker)
        return Response(serializer.data)
