from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


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


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@api_view(["POST"])
def search(request):
    query = request.data.get("query", "")

    if query:
        sneakers = Sneaker.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        serializer = SneakerSerializer(sneakers, many=True)
        return Response(serializer.data)
    else:
        return Response({"sneakers": []})
