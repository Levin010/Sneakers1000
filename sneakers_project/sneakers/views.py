from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Sneaker, Category
from .serializers import SneakerSerializer, CategorySerializer

from django.http import JsonResponse
from django.conf import settings
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


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


def debug_media(request):
    media_root = settings.MEDIA_ROOT
    uploads_path = os.path.join(media_root, "uploads")

    debug_info = {
        "media_root": media_root,
        "media_root_exists": os.path.exists(media_root),
        "uploads_path": uploads_path,
        "uploads_path_exists": os.path.exists(uploads_path),
        "media_files": [],
    }

    if os.path.exists(uploads_path):
        debug_info["media_files"] = os.listdir(uploads_path)

    return JsonResponse(debug_info)


def debug_cloudinary(request):
    debug_info = {
        "cloudinary_cloud_name": os.getenv("CLOUDINARY_CLOUD_NAME"),
        "cloudinary_api_key": os.getenv("CLOUDINARY_API_KEY"),
        "cloudinary_api_secret": bool(os.getenv("CLOUDINARY_API_SECRET")),
        "default_file_storage": getattr(settings, "DEFAULT_FILE_STORAGE", "Not set"),
        "installed_apps": "cloudinary_storage" in settings.INSTALLED_APPS,
        "cloudinary_in_apps": "cloudinary" in settings.INSTALLED_APPS,
    }
    return JsonResponse(debug_info)


def debug_storage_test(request):
    try:
        test_file = ContentFile(b"test content", name="test.txt")
        saved_name = default_storage.save("test_upload.txt", test_file)
        file_url = default_storage.url(saved_name)

        return JsonResponse(
            {
                "storage_class": str(type(default_storage)),
                "saved_name": saved_name,
                "file_url": file_url,
                "is_cloudinary": "cloudinary.com" in file_url,
            }
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e),
                "storage_class": str(type(default_storage)),
            }
        )
