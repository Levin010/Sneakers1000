from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from sneakers_project.sneakers.views import (
    debug_media,
    debug_cloudinary,
    debug_storage_test,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", (include("djoser.urls"))),
    path("api/v1/", (include("djoser.urls.authtoken"))),
    path("api/v1/", include("sneakers_project.sneakers.urls")),
    path("api/v1/", include("sneakers_project.order.urls")),
    path("debug/media/", debug_media, name="debug_media"),
    path("debug/cloudinary/", debug_cloudinary, name="debug_cloudinary"),
    path("debug/storage-test/", debug_storage_test, name="debug_storage_test"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
